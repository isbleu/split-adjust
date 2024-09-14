# split-adjust
* yfinance stock price data split adjust backward
  
* sometimes you may need an original price,but unfortunately yfinance provide the HLOC prices adjusted for split, users may want to adjust backward for some reason to get the original prices. at this time, it is the piece of code that may help with you.

* the single function returns a dataframe structure that contains adj. HLOC(i.e. adj. Close adj. High ...) and at the same time it reverse the already split-adjusted HLOC to unadjusted, original ones if the 'adjustback_for_split' boolean value is set to True
