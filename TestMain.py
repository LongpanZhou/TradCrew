from Stock.Stock import Stock
from AnalysisScripts.PricePred import pricePred

AAPL = Stock("AAPL")
print(AAPL.data)
print(AAPL.data['Adj Close'].pct_change())

pricePred(AAPL, 1)