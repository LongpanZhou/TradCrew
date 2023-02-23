import math

import numpy as np
import pandas as pd
from tqdm import tqdm
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Stock.Stock import Stock

def corrFinder(s: Stock):
    folder = input("Input the Stock Exchange")
    data_dir = "../Data"f'{folder}'
    types = input("Please input the type correlation looking for: Neg, Pos, Neu. (Type all 3 to diaplay all types)")
    save = input("Please input if you want to save to a save. Y/N")
    if save:
        path = input("Please input path you wanted to be saved in.")
        if not os.path.exists(path):
            path = "../Analysis"
            print("Path does not exist. Default to \"Analysis\" folder.")

    csv_files = []
    neg = []
    pos = []
    neu = []

    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endwith(".csv"):
                csv_files.append(os.path.join(root,file))

    for file in tdqm(csv_files):
        df = pd.read_csv(file)
        daily_returns = [_ * 100 for _ in df['Adj Close'].pct_change() if not math.isnan(_)]
        cov = np.cov(s.pct,daily_returns)
        var = np.var(daily_returns)
        cor = cov/(math.sqrt(var)*s.std)

        if -0.1 < cor < 0.1:
            neu.append()
        elif cor > 0.8:
            pos.append()
        elif cor > -0.8:
            neg.append()

    for type in types.strip(" ").split(","):
        match type:
            case "Neg":
                pass
            case "Pos":
                pass
            case "Neu":
                pass

    def save():
        pass
