import math
import numpy as np
import pandas as pd
from tqdm import tqdm
import sys
import time
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Stock.Stock import Stock

def corrFinder(s: Stock):
    folder = input("Input the Stock Exchange: ")
    data_dir = "../Data/"f'{folder.upper()}'
    types = input("Please input the type correlation looking for: Neg, Pos, Neu. (Type all 3 to diaplay all types) ")
    save = input("Please input if you want to save to a save: Y/N ")
    if save.upper() == "Y":
        path = input("Please input path you wanted to be saved in: ")
        if not os.path.exists(path):
            path = "../Analysis"
            print("Path does not exist. Default to \"Analysis\" folder.")
        if not os.path.exists(path):
            os.makedirs(path)
        time.sleep(2)

    csv_files = []
    tickers = []
    neg = []
    pos = []
    neu = []

    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith(".csv"):
                csv_files.append(os.path.join(root,file))
                tickers.append(file.strip(".csv"))

    for i, file in enumerate(tqdm(csv_files)):
        df = pd.read_csv(file)
        daily_returns = [_ * 100 for _ in df['Adj Close'].pct_change() if not math.isnan(_)]
        try:
            cov = np.cov(s.pct, daily_returns)[0][1]
            var = np.var(daily_returns)
            cor = cov / (math.sqrt(var) * s.std())
            print(f"Processing {file}")

            if -0.1 < cor < 0.1:
                neu.append(tickers[i])
            elif cor > 0.8:
                pos.append(tickers[i])
            elif cor > -0.8:
                neg.append(tickers[i])
        except:
            print(f"Skipping {file}")

    for corType in types.upper().strip(" ").split(","):
        match corType:
            case "NEG":
                print(f'Negtive Correlated Stocks:{neg}')
                try:
                    file_path = os.path.join(path,f'{s.ticker}_{folder}_Neg.csv')
                    save_file(save,neg,file_path)
                except:
                    print("Failed to save")
            case "POS":
                print(f'Negtive Correlated Stocks:{pos}')
                try:
                    file_path = os.path.join(path, f'{s.ticker}_{folder}_Pos.csv')
                    save_file(save, pos, file_path)
                except:
                    print("Failed to save")
            case "NEU":
                print(f'Negtive Correlated Stocks:{neu}')
                try:
                    file_path = os.path.join(path, f'{s.ticker}_{folder}_Neu.csv')
                    save_file(save, neu, file_path)
                except:
                    print("Failed to save")

def save_file(YN,correlation,file_path):
    if YN.upper() == "Y":
        pd.DataFrame(correlation).to_csv(file_path)