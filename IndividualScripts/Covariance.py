import math

import numpy as np
import yfinance as yf

# Define the stock tickers
tickers = ["^GSPC", "^DJI", "^IXIC"]

# Get the historical stock prices
data = {}
for i in tickers:
    name = yf.Ticker(i).info['longName'].split(",")[0]
    data[f'{name}'] = yf.download(i, period="1y").resample("D").last()

# Ask user to input
while True:
    stock = input("Enter your stock ticker symbol:")
    try:
        if stock == "Q": break
        stock_data = yf.download(stock, period="1y").resample("D").last()
        stock_name = yf.Ticker(stock).info['longName'].split(",")[0]
        break
    except:
        print("Invalid stock symbol. Please re-enter:")
        print("Or type Q to quit")

#Load stock into data
data[f'{stock_name}'] = stock_data

# Plot the daily percentage change
return_change = []
for key in data:
    return_change.append([_ * 100 for _ in data[key]['Adj Close'].pct_change() if _ != 0 and not math.isnan(_)])

#calculate cov compare to each index
cov = [0,0,0,-1]

#fix range
return_change[0].remove()

#Display matching days
for i, key in enumerate(data):
    cov[i] = np.cov(return_change[3],return_change[i])[0][1]
    print("Days matched "f'{stock_name}'" with "f'{key}'": "f'{cov[i]}')