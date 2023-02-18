import pandas as pd
import yfinance as yf
from Stock.Stock import Stock

a = Stock("QQQ")
print(a.var())