import math
import numpy as np
import yfinance as yf


class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = yf.download(self.ticker, period="1y").resample("D").last()
        #self.name = yf.Ticker(self.ticker).info['longName'].split(",")[0]
        self.pct = [_ * 100 for _ in self.data['Adj Close'].pct_change() if not math.isnan(_)]

    def mean(self):
        price = [_ for _ in self.data['Adj Close'] if not math.isnan(_)]
        return np.median(price)

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

    def beta(self):
        tickers = ["^GSPC", "^DJI", "^IXIC"]
        data = {}
        daily_returns = []
        var = [0, 0, 0]
        cov = [0, 0, 0]
        cor = [0, 0, 0]

        for i in tickers:
            # name = yf.Ticker(i).info['longName'].split(",")[0]
            data[f'{i}'] = yf.download(i, period="1y").resample("D").last()

        for i, key in enumerate(data):
            daily_returns.append([_ * 100 for _ in data[key]['Adj Close'].pct_change() if not math.isnan(_)])
            var[i] = np.var(daily_returns[i])

        for i, key in enumerate(data):
            cov[i] = np.cov(self.pct, daily_returns[i])[0][1]
            cor[i] = cov[i] / (math.sqrt(self.var()) * math.sqrt(var[i]))
            beta.append(cov[i] / var[i])
            print("Beta of "f'{self.ticker}'" with "f'{key}'": "f'{beta[i]}')

    def negativeCorrelationFinder(self):
        pass

    def postiveCorrelationFinder(self):
        pass

    def neutrualCorrelationFinder(self):
        pass