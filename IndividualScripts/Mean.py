import math

import yfinance as yf
import numpy as np

# Ask user to input
while True:
    stock = input("Enter your stock ticker symbol:")
    try:
        if stock == "Q": break
        stock_data = yf.download(stock, period="1y").resample("D").last()
        price_data = [_ for _ in stock_data['Close'] if not math.isnan(_)]
        #stock_name = yf.Ticker(stock).info['longName'].split(",")[0]
        break
    except:
        print("Invalid stock symbol. Please re-enter:")
        print("Or type Q to quit")

print(np.median(price_data))