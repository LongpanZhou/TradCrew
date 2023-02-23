import pandas as pd
import yfinance as yf
from Downloader import downloadData
from Extractor import extractTickers

file = "NYSE.csv"
tickers = extractTickers(file)
downloadData(tickers,"NYSE")