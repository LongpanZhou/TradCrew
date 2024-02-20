import pandas_ta as ta
import yfinance as yf
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Stock.Stock import Stock

def RSI(s: Stock, years):
    #download data
    data = yf.download(tickers=s.ticker, period=f'{years}y')

    data['EMA'] = ta.ema(data.Close, length = 200)
    data['RSI'] = ta.rsi(data.Close, length = 2)
    data['ADX'] = ta.adx(data.High, data.Low, data.Close, length=14)

    data.dropna(inplace=True)
    data.reset_index(inplace=True)

    add_ema_singal(data,6)


def add_ema_singal(df, backcandles):
    ema_singal = [0]*len(df)
    for row in range(backcandles, len(df)):
        upt = 1
        dnt = 1
        for i in range(row-backcandles, row+1):
            if df.High[i]>=df.EMA[i]:
                dnt = 0
            if df.Low[i]<=df.EMA[i]:
                upt = 0
        if upt == 1 and dnt == 1:
            print("Stock is equal to EMA")
            ema_singal[row] = -1
        elif upt == 1: ema_singal[row] = 2
        elif dnt == 1: ema_singal[row] = 1