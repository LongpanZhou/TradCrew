# TradeCrew
 This project, developed last year, aimed to assist in stock analysis for managing personal investment portfolios, including Tax-Free Savings Accounts (TFSA) and non-registered accounts. It provided features for portfolio management, stock analysis, risk assessment, performance metrics, and data visualization.

> [!NOTE]
> Project is initially abandoned as I found Job for Summer, not sure if I will maintain this project (maybe from time to time).
 
> [!WARNING]
> DO NOT USE THE TRADING STRATEGY AS YOUR PERSONAL STRATEGY.

## Setting Up Environment
1. This project is developed using PyCharm, the `.idea` Folder is included for virtual environment. It is recommended to use Jet Brain product to open this.
2. You can also install the `requirements.txt` on your global interpreter by using `pip install -r requirements.txt`.


## Structure
The project includes 4 parts, AnalysisScripts, IndividualScripts, Stock, Tickers, and TradingStra.

* ### AnalysisScripts
  * CorrelationFiner
  <br/> Precondition: `NYSE` folder must be populated with `Downloader` and `Extractor` (Tickers folder).
  <br/> This script is used to find stocks with similar correlation with input `stock exchange` (for example NYSE), then displays it, options including `POS: Postively related stocks`, `NEG: Negatively related stocks`, `NEU: Non-related stocks`.
  <br/><br/>Usage:
    ```commandline
    python CorrelationFiner.py
    ```
    Output:
    ```commandline
    Python 3.9 (match cases not supported) 
    :) Update later
    ```
  * DelayCorrelationFinder
  <br/> This script is used to find stocks with delayed correlations with given number of `days` and `stock exchange`, it will display the correlated stock with the number of days delayed.
  <br/><br/>Usage: Under AnalysisScripts Folder
    ```commandline
    python DelayCorrelationFinder.py
    ```
    Output:
    ```commandline
    :P Again, update later...
    ```
  * PricePrediction
  
* ### IndividualScripts
  * Beta
  * CorrelationIndex
  * CorrelationStocks
  * Covariance
  * Mean
  * PatternMatchingIndex
  * PercentageChangeD
  * PercentageChangeY
  * Variance
* ### Stock
  * Stock Class
* ### Tickers
  * Downloader
  * Extractor
* ### TradingStra
  * Hedge
  * RSI Long


*Not completed.... To be continued...*
### AnalysisScripts
* CorrelationFiner 
  <br/>
* DelayCorrelationFinder
* PricePrediction

### IndividualScripts
* Beta
* CorrelationIndex
* CorrelationStocks
* Covariance
* Mean
* PatternMatchingIndex
* PercentageChangeD
* PercentageChangeY
* Variance

### Stock
* Stock Class
<br/> This is the main class to store a Stock's information, it has attributes `self.ticker, self.data, self.pct`.
<br/><br/> Functions of this class in include: 
<br/> `mean(): calculate the median of the stock`
<br/> `var(): calculate the variance of a stock`
<br/> `std(): calculate the standard diviation of a stock`
<br/> `cov(another_stock): calculate the covariance of a stock with another stock`
<br/> `cor(another_stock): calculate the correlation of a stock with another stock`
<br/> `beta(): calculate the beta of a stock with comparsion for ^GSPC(S&P 500), ^DJI(Dow Jones Index), ^IXIC(Nasdaq Index).`
<br/> `negativeCorrelationFinder(): N/A (Not implemented)`
<br/> `postiveCorrelationFinder(): N/A`
<br/> `neutrualCorrelationFinder(): N/A`
<br/><br/> Usage:
  ```python
  #TestMain.py
  AAPL = Stock("AAPL")
  print(AAPL.data)
  print(AAPL.data['Adj Close'].pct_change())
  ```

### Tickers
* Downloader
<br/> This is the downloader class, which contains one function - `downloadData(tickeer,FolderName)`. This will take *tickers* and download its data to *FolderName*.
<br/><br/> Usage:
  ```python
  from Downloader import downloadData
  tickers = ['AAPL']
  downloadData(tickers,"NYSE")
  ```
* Extractor
<br/> This is the extractor class, which contains one function - `extractTickers(file)`. This will take the .csv file and extract all the tickers column.
<br/><br/> Usage:
  ```python
  from Extractor import extractTickers
  file = "NYSE.csv"
  tickers = extractTickers(file)
  ```
* .CSV Files
<br/> Some of the .csv files are given in the project folder, for example FTSE.csv, Nasdaq.csv, NYSE.csv etc. Users can also download these ticker csv files from online. (make sure to change column name to `Ticker`)
### TradingStra
  * Hedge
  * RSI Long

### TODOS:
[] Finish readme.md