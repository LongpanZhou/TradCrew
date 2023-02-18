import pandas as pd
import yfinance as yf
from Tickers.Downloader import downloadData
from Tickers.Extractor import extractTickers

file = "Tickers/FTSE.csv"
tickers = extractTickers(file)
downloadData(tickers)