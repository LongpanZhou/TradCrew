import math
import numpy as np
import yfinance as yf

# Define the stock tickers
tickers = ["^GSPC", "^DJI", "^IXIC"]

# Get the historical stock prices
data = {}
for i in tickers:
    #name = yf.Ticker(i).info['longName'].split(",")[0]
    data[f'{i}'] = yf.download(i, period="1y").resample("D").last()

# Ask user to input
while True:
    stock = input("Enter your stock ticker symbol:")
    try:
        if stock == "Q": break
        stock_data = yf.download(stock, period="1y").resample("D").last()
        #stock_name = yf.Ticker(stock).info['longName'].split(",")[0]
        data[f'{stock}'] = stock_data
        break
    except:
        print("Invalid stock symbol. Please re-enter:")
        print("Or type Q to quit")

# Plot the daily percentage change
daily_returns = []

#calculate cov, var and cor
cov = [0,0,0,0]
var = [0,0,0,0]
cor = [0,0,0,0]

for i, key in enumerate(data):
    daily_returns.append([_ * 100 for _ in data[key]['Adj Close'].pct_change() if not math.isnan(_)])

    var[i] = np.var(daily_returns[i])

#Display
for i, key in enumerate(data):
    cov[i] = np.cov(daily_returns[3], daily_returns[i][:len(daily_returns[3])])[0][1]
    cor[i] = cov[i]/(math.sqrt(var[3])*math.sqrt(var[i]))
    print("Correlation of "f'{stock}'" with "f'{key}'": "f'{cor[i]}')