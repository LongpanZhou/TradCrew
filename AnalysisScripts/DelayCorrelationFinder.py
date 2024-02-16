import math
import numpy as np
import pandas as pd
from tqdm import tqdm
import sys
import time

import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import warnings
warnings.filterwarnings("ignore", message="The default fill_method='pad' in Series.pct_change is deprecated.*")

from Stock.Stock import Stock

def delayedCorrFinder(s: Stock, dir):
    folder = input("Input the Stock Exchange: ")
    data_dir = f'{dir}/{folder.upper()}'
    days = int(input("Input the number of days you want to perform the delayed analysis: ")) + 1
    save = input("Please input if you want to save to a save: Y/N ")
    if save.upper() == "Y":
        path = input("Please input path you wanted to be saved in: ")
        if not os.path.exists(path):
            path = "Analysis"
            print("Path does not exist. Default to \"Analysis\" folder.")
        if not os.path.exists(path):
            os.makedirs(path)
        time.sleep(2)

    csv_files = []
    tickers = []
    pos = []

    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith(".csv"):
                csv_files.append(os.path.join(root,file))
                tickers.append(file.strip(".csv"))

    for day in tqdm(range(days)):
        pos.append([])
        for i, file in tqdm(enumerate(csv_files)):
            df = pd.read_csv(file)
            daily_returns = [_ * 100 for _ in df['Adj Close'].pct_change() if not math.isnan(_)]
            daily_returns = daily_returns[day:]
            try:
                cov = np.cov(s.pct[:len(s.pct)-day], daily_returns)[0][1]
                var = np.var(daily_returns)
                cor = cov / (math.sqrt(var) * math.sqrt(np.var(s.pct[:len(s.pct)-days])))
                print(f"Processing {file} with {day} day delayed")

                if cor > 0.80:
                    pos[day].append(tickers[i])
            except:
                print(f"Skipping {file}")

    for day, _ in enumerate(pos):
        print(f'Day {day}:{_}')

    if save.upper() == "Y":
        try:
            file_path = os.path.join(path, f'{s.ticker}_{folder}_delayed.csv')
            save_file(save, pos, file_path)
        except:
            print("Failed to save")

    return pos

def save_file(YN,correlation,file_path):
    if YN.upper() == "Y":
        pd.DataFrame(correlation).to_csv(file_path)