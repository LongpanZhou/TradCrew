import numpy as np
import yfinance as yf


class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        try:
            self.data = stock_data = yf.download(self.ticker, period="1y").resample("D").last()
            self.name = yf.Ticker(self.ticker).info['longName'].split(",")[0]
            self.pct = [_ * 100 for _ in stock_data['Adj Close'].pct_change() if _ != 0 and not np.isnan(_)]
        except:
            print("Oops")

    def mean(self):
        return yf.Ticker(self.ticker).info['regularMarketPrice']

    def var(self):
        return np.var(self.pct)

    def std(self):
        return np.std(self.pct)

    def cov(self, another_stock):
        if not isinstance(another_stock, Stock):
            raise TypeError('Parameter should be of type Stock')
        if len(self.pct) == len(another_stock.pct):
            return np.cov(self.pct, another_stock.pct)
        else:
            min_len = min(len(self.pct), len(another_stock.pct))
            return np.cov(self.pct[:min_len], another_stock.pct[:min_len])

    def cor(self, another_stock):
        if not isinstance(another_stock, Stock):
            raise TypeError('Parameter should be of type Stock')
        return self.cov(another_stock) / (np.sqrt(self.var()) * np.sqrt(another_stock.var()))