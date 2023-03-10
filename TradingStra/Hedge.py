import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_ta as ta
import yfinance as yf

from backtesting import Strategy
from backtesting import Backtest
import backtesting

data = yf.download("EURUSD=X",period='60d',interval='5m')

#define parameters
grid_distance = 0.005
midprice = 1.065

#generate a grid from 0.965-1.165 with 0.005distance
def generate_grid(midprice, grid_distance, grid_range):
    return(np.arange(midprice-grid_range,midprice+grid_range,grid_distance))

grid = generate_grid(midprice=midprice,grid_distance=grid_distance,grid_range=0.1)

#set to default signal to 1 if any grid numbers is between daily low and daily high
signal = [1 if any(row.Low < p < row.High for p in grid) else 0 for index, row in data.iterrows()]

#fliter data
data["signal"]=signal
data[data["signal"]==1]

#make a copy of data
dfpl = data[:].copy()
def SIGNAL():
    return dfpl.signal

#calculate Average True Range
dfpl['ATR'] = ta.atr(high=dfpl.High,low=dfpl.Low,close=dfpl.Close, length=16)
dfpl.dropna(inplace=True)

class GridHedge(Strategy):
    n = 50
    def init(self):
        super().init()
        self.signal = self.I(SIGNAL)

    def next(self):
        super().next()
        slatr = 1.5*grid_distance
        Ratio = 0.5

        if self.signal==1 and len(self.trades)<=100:
            #short position
            sl1 = self.data.Close[-1] + slatr
            tp1 = self.data.Close[-1] - slatr*Ratio
            self.sell(sl=sl1, tp=tp1, size=self.n)

            #long position
            sl1 = self.data.Close[-1] - slatr
            tp1 = self.data.Close[-1] + slatr*Ratio
            self.buy(sl=sl1, tp=tp1, size=self.n)

#running simulation
bt = Backtest(dfpl, GridHedge, cash=1000, margin=1/100, commission=.0005, hedging=True, exclusive_orders=False)
stat = bt.run()
stat
print(stat)