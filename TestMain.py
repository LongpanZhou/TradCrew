from Stock.Stock import Stock
import os
import pandas as pd
from tqdm import tqdm
import math

AAPL = Stock("AAC")
print(AAPL.data)
print(AAPL.data['Adj Close'].pct_change())