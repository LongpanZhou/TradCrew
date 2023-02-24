import pandas as pd
import yfinance as yf
from tqdm import tqdm
import os

def downloadData(tickers,FolderName):
    directory = '../Data/'f'{FolderName}'
    if not os.path.exists(directory):
        os.makedirs(directory)
    for ticker in tqdm(tickers):
        try:
            data = yf.download(ticker,period='1y').resample("D").last()
            file_path = os.path.join(directory, f'{ticker}.csv')
            data.to_csv(file_path)
            print(f'{ticker}.csv has been successfully saved.')
        except:
            print("Error occurred during downloading/saving "f'{ticker}'".csv")