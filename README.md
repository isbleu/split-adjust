# Split-Adjust for Yfinance data

* yfinance data adjustment for split and dividend
  
* sometimes you may need an original price,but unfortunately yfinance provide the OHLC prices adjusted for split, users may want to adjust backward for some reason to get the original prices. at this time, it is the piece of code that may help with you.

* the single function returns a dataframe structure that contains adj. OHLC(i.e. adj. Close adj. High ...) and at the same time it can reverse the already split-adjusted OHLC to the unadjusted, original ones if the 'adjustback_for_split' boolean value is set to True

# Quick Start
import your yfinance data,with `actions = True`
```python
import yfinance as yf

msft = yf.download("MSFT",actions = True)
# warning: DON'T use history(),the data is somehow incorrect for adjustment 

```
call the function with `adjustback_for_split = True` if you want to get the original prices.
```python
msft = adjust_yfinance_stock_price(msft,adjustback_for_split = True)
```
