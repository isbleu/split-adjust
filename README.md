# Split-Adjust for Yfinance data

* yfinance data adjustment for split and dividend
  
* sometimes you may need an original price,but unfortunately yfinance provide the OHLC prices adjusted for split, users may want to adjust backward for some reason to get the original prices. at this time, it is the piece of code that may help with you.

* the single function returns a dataframe structure that contains adj. OHLC(i.e. adj. Close adj. High ...) and at the same time it can reverse the already split-adjusted OHLC to the unadjusted, original ones if the 'adjustback_for_split' boolean value is set to True

# Quick Start
* 1,import your yfinance data,with `actions = True`
```python
import yfinance as yf

msft = yf.download("MSFT",actions = True)

# warning: DON'T use history(),the data is somehow incorrect for adjustment 
```
* 2,call the function with `adjustback_for_split = True` if you want to get the original prices.
```python
msft = adjust_yfinance_stock_price(msft,adjustback_for_split = True)
```

## Output example for msft:
<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Adj Close</th>
      <th>Volume</th>
      <th>Dividends</th>
      <th>Stock Splits</th>
      <th>Split Ratio</th>
      <th>Adj. Close</th>
      <th>Adj. Volume</th>
      <th>Adj. Open</th>
      <th>Adj. High</th>
      <th>Adj. Low</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1986-03-13</th>
      <td>25.500096</td>
      <td>29.250144</td>
      <td>25.500096</td>
      <td>27.999936</td>
      <td>0.059946</td>
      <td>3582600.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.059946</td>
      <td>1.031789e+09</td>
      <td>0.054594</td>
      <td>0.062623</td>
      <td>0.054594</td>
    </tr>
    <tr>
      <th>1986-03-14</th>
      <td>27.999936</td>
      <td>29.500128</td>
      <td>27.999936</td>
      <td>28.999872</td>
      <td>0.062087</td>
      <td>1070000.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.062087</td>
      <td>3.081600e+08</td>
      <td>0.059946</td>
      <td>0.063158</td>
      <td>0.059946</td>
    </tr>
    <tr>
      <th>1986-03-17</th>
      <td>28.999872</td>
      <td>29.750112</td>
      <td>28.999872</td>
      <td>29.500128</td>
      <td>0.063158</td>
      <td>462400.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.063158</td>
      <td>1.331712e+08</td>
      <td>0.062087</td>
      <td>0.063694</td>
      <td>0.062087</td>
    </tr>
    <tr>
      <th>1986-03-18</th>
      <td>29.500128</td>
      <td>29.750112</td>
      <td>28.499904</td>
      <td>28.749888</td>
      <td>0.061552</td>
      <td>235300.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.061552</td>
      <td>6.776640e+07</td>
      <td>0.063158</td>
      <td>0.063694</td>
      <td>0.061017</td>
    </tr>
    <tr>
      <th>1986-03-19</th>
      <td>28.749888</td>
      <td>28.999872</td>
      <td>27.999936</td>
      <td>28.249920</td>
      <td>0.060482</td>
      <td>166300.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.060482</td>
      <td>4.789440e+07</td>
      <td>0.061552</td>
      <td>0.062087</td>
      <td>0.059946</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2024-09-09</th>
      <td>407.239990</td>
      <td>408.649994</td>
      <td>402.149994</td>
      <td>405.720001</td>
      <td>405.720001</td>
      <td>15295100.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>405.720001</td>
      <td>1.529510e+07</td>
      <td>407.239990</td>
      <td>408.649994</td>
      <td>402.149994</td>
    </tr>
    <tr>
      <th>2024-09-10</th>
      <td>408.200012</td>
      <td>416.329987</td>
      <td>407.700012</td>
      <td>414.200012</td>
      <td>414.200012</td>
      <td>19594300.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>414.200012</td>
      <td>1.959430e+07</td>
      <td>408.200012</td>
      <td>416.329987</td>
      <td>407.700012</td>
    </tr>
    <tr>
      <th>2024-09-11</th>
      <td>415.500000</td>
      <td>423.989990</td>
      <td>409.579987</td>
      <td>423.040009</td>
      <td>423.040009</td>
      <td>19266900.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>423.040009</td>
      <td>1.926690e+07</td>
      <td>415.500000</td>
      <td>423.989990</td>
      <td>409.579987</td>
    </tr>
    <tr>
      <th>2024-09-12</th>
      <td>423.309998</td>
      <td>427.369995</td>
      <td>419.750000</td>
      <td>427.000000</td>
      <td>427.000000</td>
      <td>17418800.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>427.000000</td>
      <td>1.741880e+07</td>
      <td>423.309998</td>
      <td>427.369995</td>
      <td>419.750000</td>
    </tr>
    <tr>
      <th>2024-09-13</th>
      <td>425.829987</td>
      <td>431.829987</td>
      <td>425.459991</td>
      <td>430.589996</td>
      <td>430.589996</td>
      <td>15861900.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>430.589996</td>
      <td>1.586190e+07</td>
      <td>425.829987</td>
      <td>431.829987</td>
      <td>425.459991</td>
    </tr>
  </tbody>
</table>
<p>9704 rows x 14 columns</p>
</div>
