import math
import numpy as np
import yfinance as yf

# Ask user to input
while True:
    stock = input("Enter your stock ticker symbol:")
    try:
        if stock == "Q": break
        stock_data = yf.download(stock, period="1y").resample("D").last()
        stock_name = yf.Ticker(stock).info['longName'].split(",")[0]
        daily_returns = [_ * 100 for _ in stock_data['Adj Close'].pct_change() if _ != 0 and not math.isnan(_)]
        variance = np.var(daily_returns)
        print(f'{stock_name}'" has variance: "f'{variance}')
        print(f'{stock_name}'" has standard deviation: "f'{math.sqrt(variance)}')
        break
    except:
        print("Invalid stock symbol. Please re-enter:")
        print("Or type Q to quit")