import yfinance as yf
import matplotlib.pyplot as plt

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
for key in data:
    percent_change = data[key]['Close'].pct_change()
    plt.plot(percent_change.index, percent_change, label=key)

plt.title(f'{stock}'" VS Indexes")
plt.legend()
plt.xlabel('Date YYYY/MM/DD')
plt.ylabel('Price %')
plt.show()