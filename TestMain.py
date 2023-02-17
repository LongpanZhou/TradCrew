import yfinance as yf
import numpy as np

# Define stock symbols and time period
stock_symbol_1 = "AAPL"
stock_symbol_2 = "MSFT"
start_date = "2022-02-07"
end_date = "2023-02-07"

# Retrieve stock data
stock_data = yf.download([stock_symbol_1, stock_symbol_2], start=start_date, end=end_date)

# Calculate daily returns
daily_returns = stock_data['Adj Close'].pct_change()

# Calculate covariance
covariance = np.cov(daily_returns[stock_symbol_1], daily_returns[stock_symbol_2])[0][1]

# Print result
print("Covariance:", covariance)