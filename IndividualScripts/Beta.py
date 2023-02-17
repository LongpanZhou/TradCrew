import math
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
percent_change = []
for key in data:
    percent_change.append(data[key]['Close'].pct_change())