import pandas as pd
import re

def extractTickers(file):
    pd_file = pd.read_csv(file)
    tickers_df = pd.DataFrame(pd_file, columns=['Ticker'])
    tickers = [re.split('[,.]', t)[0] for t in tickers_df['Ticker'].tolist()]
    return tickers