# import pip
# pip.main(['install', 'matplotlib'])

import pandas_datareader as pdr
import datetime as dt
import matplotlib.pyplot as plt

import quandl
ticker = quandl.get("WIKI/AAPL", start_date="2016-1-1", end_date="2017-6-6")
ticker['14-high'] = ticker['High'].rolling(14).max()
ticker['14-low'] = ticker['Low'].rolling(14).min()
ticker['%K'] = (ticker['Close'] - ticker['14-low'])*100/(ticker['14-high'] - ticker['14-low'])
ticker['%D'] = ticker['%K'].rolling(3).mean()
ax = ticker[['%K', '%D']].plot()
ticker['Adj. Close'].plot(ax=ax, secondary_y=True)
ax.axhline(20, linestyle='--', color="r")
ax.axhline(80, linestyle="--", color="r")
plt.show()

# ticker = pdr.get_data_yahoo("AAPL", dt.datetime(2020,1,1), dt.datetime.now())
#
# import pandas as pd
# data = pd.Series([1,2,3])
#
print(ticker)