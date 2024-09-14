'''
Created on 2024 Sep 8
### 调整yfinance数据
* 1，把split为0的值变为1,还原close 用从后往前累乘split
* 2，判断是否需要adjustback_for_split
* 3，复制stock里的close到adj. close列
* 4，如果需要还原close open等 用从后往前的split的cumprod * 这些值
* 5，从后往前reversed for loop 先算出 adj_ratios = adj_close_t1 / close_t1再用 除权的当日close * adj_ratios
* 6，其他open等也按照同样的方式 除权的当日open * adj_ratios
@author: iswx
'''
import pandas as pd
import numpy as np

def adjust_yfinance_stock_price(stock,adjustback_for_split=False):
    stock = stock.copy()

    if adjustback_for_split == True: #调整回未除权价格
        stock['Split Ratio'] = np.where(stock['Stock Splits'] == 0 , 1,stock['Stock Splits'] )
        splits_t1 = stock['Split Ratio'].shift(-1).fillna(stock['Split Ratio'])
        splits_t1_reversed_cumrod = np.cumprod(splits_t1[::-1])[::-1] #cumulative product backward
        stock['Open'] *= splits_t1_reversed_cumrod
        stock['Close'] *= splits_t1_reversed_cumrod
        stock['High'] *= splits_t1_reversed_cumrod
        stock['Low'] *= splits_t1_reversed_cumrod
        stock['Volume'] /= splits_t1_reversed_cumrod #把成交量除以split 还原volume
    else: #default setting to not adjust back for split
        stock['Split Ratio'] = 1 #该数据已经调整过split了
        splits_t1 = stock['Split Ratio'].shift(-1).fillna(stock['Split Ratio'])
        splits_t1_reversed_cumrod = np.cumprod(splits_t1[::-1])[::-1]
    
    stock['Adj. Close'] = stock['Close']#初始化Adj. Close
    
    divs_t1 = stock['Dividends'].shift(-1).fillna(stock['Dividends'])
    closes_exdiv = (stock['Close'] - divs_t1) / splits_t1
    
    stock['Adj. Volume'] = stock['Volume'] * splits_t1_reversed_cumrod
    
    adj_ratios = np.ones(len(stock))
    for t in reversed(range(len(stock)-1)):
        close_t1 = stock.loc[stock.index[t+1],'Close']
        adj_close_t1 = stock.loc[stock.index[t+1],'Adj. Close']
        adj_ratios[t] = adj_close_t1 / close_t1
        stock.loc[stock.index[t],'Adj. Close'] = closes_exdiv.loc[stock.index[t]] * adj_ratios[t]

    stock['Adj. Open'] = (stock['Open'] - divs_t1) / splits_t1 * adj_ratios
    stock['Adj. High'] = (stock['High'] - divs_t1) / splits_t1 * adj_ratios
    stock['Adj. Low'] = (stock['Low'] - divs_t1) / splits_t1 * adj_ratios
    return stock