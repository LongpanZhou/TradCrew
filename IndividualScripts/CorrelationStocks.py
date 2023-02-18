import math
import numpy as np
import yfinance as yf

#Initialize data
data = {}
cov = []
var = []
cor = []
daily_returns = []

# Ask user to input
while True:
    stock = input("Enter your primary stock ticker symbol:")
    try:
        if stock == "Q": break
        stock_data = yf.download(stock, period="1y").resample("D").last()
        stock_name = yf.Ticker(stock).info['longName'].split(",")[0]
        data[f'{stock_name}'] = stock_data
        break
    except:
        print("Invalid stock symbol. Please re-enter:")
        print("Or type Q to quit")

while True:
    stocks = input("Enter your secondary stock ticker symbols(split with \" \"):").split(" ")
    try:
        if stocks == "Q": break
        for i in stocks:
            if i:
                current = i
                current_name = yf.Ticker(i).info['longName'].split(",")[0]
                if current_name not in data.keys():
                    current_data = yf.download(i, period="1y").resample("D").last()
                    data[f'{current_name}'] = current_data
                else:
                    print(f'{i}'" is already loaded in data")
            else:
                current = "No input"
        break
    except:
        print(f'{current}'" is invalid")
        print("Or type Q to quit")

min_len = 365
for i, key in enumerate(data):
    daily_returns.append([_ * 100 for _ in data[key]['Adj Close'].pct_change() if _ != 0 and not math.isnan(_)])
    min_len = min(len(daily_returns[i]),min_len)

for i, key in enumerate(data):
    cov.append(np.cov(daily_returns[0], daily_returns[i][:min_len])[0][1])
    var.append(np.var(daily_returns[i]))
    cor.append(cov[i]/(math.sqrt(var[0])*math.sqrt(var[i])))
    print("The correlation between "f'{stock_name}'" and "f'{key}'": "f'{cor[i]}')