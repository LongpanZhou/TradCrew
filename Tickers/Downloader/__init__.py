import pandas as pd
import yfinance as yf
import os

def downloadData(tickers):
    directory = 'Data'
    if not os.path.exists(directory):
        os.makedirs(directory)
    for ticker in tickers:
        try:
            data = yf.download(ticker,period='1y')
            file_path = os.path.join(directory, f'{ticker}.csv')
            data.to_csv(file_path)
            print(f'{ticker}.csv has been successfully saved.')
        except:
            print("Error occurred during downloading/saving "f'{ticker}'".csv")