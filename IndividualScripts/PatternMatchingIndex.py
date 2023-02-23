import math
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
        break
    except:
        print("Invalid stock symbol. Please re-enter:")
        print("Or type Q to quit")

#Load stock into data
data[f'{stock}'] = stock_data

# Plot the daily percentage change
percent_change = []
for key in data:
    percent_change.append(data[key]['Close'].pct_change())

#calculate closest index
Days = [0,0,0,-1]
for i in range(len(percent_change[0])):
    daily_change = percent_change[3][i]
    if daily_change != 0 and not math.isnan(daily_change):
        min_list = []
        min_list.append(daily_change - percent_change[0][i])
        min_list.append(daily_change - percent_change[1][i])
        min_list.append(daily_change - percent_change[2][i])
        num, num_index = min(min_list), min_list.index(min(min_list))
        Days[num_index]+=1

#Display matching days
for i, key in enumerate(data):
    print("Days matched "f'{stock}'" with "f'{key}'": "f'{Days[i]}')