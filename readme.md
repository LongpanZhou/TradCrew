# TradeCrew
 This project, developed last year, aimed to assist in stock analysis for managing personal investment portfolios, including Tax-Free Savings Accounts (TFSA) and non-registered accounts. It provided features for portfolio management, stock analysis, risk assessment, performance metrics, and data visualization.

> [!NOTE]
> Project is initially abandoned as I found Job for Summer, not sure if I will maintain this project (maybe from time to time).
 
> [!WARNING]
> DO NOT USE THE TRADING STRATEGY AS YOUR PERSONAL STRATEGY.

## Setting Up Environment
1. This project is developed using PyCharm, the `.idea` Folder is included for virtual environment. It is recommended to use Jet Brain product to open this.
2. You can also install the `requirements.txt` on your global interpreter by using `pip install -r requirements.txt`.
3. If you only want to use certain script from this project, you can refer to the `requirements.txt` to install the requirements you need.
    ```text
    #Stock class, Tickers, Indivual Scripts, (Part) AnalysisScripts
    numpy
    pandas
    yfinance
    tqdm
    
    #Trading Stra, PricePred
    matplotlib
    pandas_ta
    backtesting
    tensorflow
    #Legacy
    sklearn
    #Present
    scikit-learn
    ```
4. Enable to support `match` case, make sure to use python version above 3.10.
    ```
    python --version
    ```

## Structure
The project includes 4 parts, AnalysisScripts, IndividualScripts, Stock, Tickers, and TradingStra.

* ### AnalysisScripts
  * CorrelationFiner
  <br/> Precondition: `NYSE` folder must be populated with `Downloader` and `Extractor`.
  <br/> This script is used to find stocks with similar correlation with input `stock exchange` (for example NYSE), then displays it, options including `POS: Postively related stocks`, `NEG: Negatively related stocks`, `NEU: Non-related stocks`.
  <br/><br/>Usage:
    ```python
    from AnalysisScripts.CorrelationFinder import corrFinder
    from Stock.Stock import Stock
    
    AAPL = Stock("AAPL")
    corrFinder(AAPL, dir='Data') #Relative Path for .csv downloaded
    ```
    Output:
    ```commandline
    Input the Stock Exchange: nyse
    Please input the type correlation looking for: Pos, Neu, Neg. (Type all 3 to display all types) Pos, Neu, Neg
    Please input if you want to save to a save: Y/N n
    Positive Correlated Stocks:[]
    Failed to save
    Neural Correlated Stocks:['SMI', 'GIM', 'GOL', 'ETP', 'CBI', 'CCZ', 'SIR', 'VVC', 'KS', 'SFE', 'MTS', 'NORD', 'CBA', 'PYT', 'CVG', 'RRTS', 'SEAS', 'JBK', 'TRMR']
    Failed to save
    Negative Correlated Stocks:['ZBK']
    Failed to save
    ```
  * DelayCorrelationFinder
  <br/> This script is used to find stocks with delayed correlations with given number of `days` and `stock exchange`, it will display the positively correlated stock with the number of days delayed.
  <br/><br/>Usage:
    ```python
    from AnalysisScripts.DelayCorrelationFinder import delayedCorrFinder
    from Stock.Stock import Stock

    QQQ = Stock("QQQ")
    delayedCorrFinder(QQQ, dir='Data')
    ```
    Output:
    ```commandline
    Input the Stock Exchange: nyse
    Input the number of days you want to perform the delayed analysis: 20
    Please input if you want to save to a save: Y/N n
    Day 0:[]
    Day 1:['MTS']
    Day 2:[]
    Day 3:[]
    Day 4:[]
    Day 5:[]
    Day 6:[]
    Day 7:[]
    Day 8:[]
    Day 9:[]
    Day 10:[]
    Day 11:[]
    Day 12:[]
    Day 13:[]
    Day 14:[]
    Day 15:[]
    Day 16:[]
    Day 17:[]
    Day 18:[]
    Day 19:[]
    Day 20:[]
    ```
  * PricePrediction
  <br/>This script is used to predict the stock price of the next day using machine learning, It uses 15 days of back candles as data for the next predicting.
  It uses mean squared error (MSE) as the loss function, Adam optimizer for training and linear activation function. The model is trained for 30 epochs with a batch size of 15 and 10% of the training data is used for validation.
    <br/><br/>Neural Network:
    ```python
    #Setting up neural network
    lstm_input = Input(shape=(backcandles, 8), name='lstm_input')
    inputs = LSTM(150, name='first_layer')(lstm_input)
    inputs = Dense(1, name='dense_layer')(inputs)
    output = Activation('linear', name='output')(inputs)
    model = Model(inputs=lstm_input, outputs=output)
    adam = optimizers.Adam()
    model.compile(optimizer=adam, loss='mse')
    model.fit(x=X_train, y=Y_train, batch_size=15, epochs=30, shuffle=True, validation_split = 0.1)
    ```
    Usage:
    ```python
    from Stock.Stock import Stock
    from AnalysisScripts.PricePred import pricePred
    
    AAPL = Stock("AAPL")
    pricePred(AAPL, 1)
    ```
    Output:
    ```commandline
    Epoch 30/30
    6/6 [==============================] - 0s 6ms/step - loss: 0.0103 - val_loss: 0.0106
    3/3 [==============================] - 0s 2ms/step
    1/1 [==============================] - 0s 8ms/step
    The prediction for the next day is: 186.31454467773438$
    ```
    Graph:
    ![Output](Images/PricePrediction.png)
### IndividualScripts
Under this folder are indivual script which can run using Python:
`python *.py`
* Beta: Calculate the market beta comparing with S&P 500, Dow Jones, and Nasdaq Index.
* CorrelationIndex: Calculate the correlation with markets by comparing with S&P 500, Dow Jones, and Nasdaq Index.
* CorrelationStocks: Calculate the correlation with another stock (ticker).
* Covariance: Calculate the covariance of a stock.
* Mean: Calculate the mean price of a stock.
* PatternMatchingIndex: Calculate the number of days ptc changes that matched with market.
* PercentageChangeD: Calculate and plot the daily changes of a stock.
* PercentageChangeY: Calculate and plot the yearly changes of a stock.
* Variance: Calculate the variance of a stock.

### Stock
* Stock Class
<br/> This is the main class to store a Stock's information, it has attributes `self.ticker, self.data, self.pct`.
<br/><br/> Functions of this class in include: 
<br/> `mean()`: calculate the median of the stock
<br/> `var()`: calculate the variance of a stock
<br/> `std()`: calculate the standard deviation of a stock
<br/> `cov(another_stock)`: calculate the covariance of a stock with another stock
<br/> `cor(another_stock)`: calculate the correlation of a stock with another stock
<br/> `beta()`: calculate the beta of a stock with comparison for ^GSPC(S&P 500), ^DJI(Dow Jones Index), ^IXIC(Nasdaq Index).
<br/> `negativeCorrelationFinder()`: Not implemented
<br/> `postiveCorrelationFinder()`: Not implemented
<br/> `neutrualCorrelationFinder()`: Not implemented
<br/><br/> Usage:
  ```python
  from Stock.Stock import Stock
  
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
* Hedge:
<br/>A class  implementing a grid-based hedging approach for trading the EUR/USD currency pair. It generates a grid of price levels around a midprice and opens positions based on specific conditions. Short positions are initiated when the signal is 1 and the number of trades is less than or equal to 100. Simultaneously, long positions are also opened.
<br/> Usage:
    ```python
    from backtesting import Strategy
    from backtesting import Backtest
    
    bt = Backtest(dfpl, GridHedge, cash=1000, margin=1/100, commission=.0005, hedging=True, exclusive_orders=False)
    stat = bt.run()
    ```
    Output:
    ```
    [*********************100%%**********************]  1 of 1 completed
     Start                     2023-11-29 01:20...
    End                       2024-02-20 04:15...
    Duration                     83 days 02:55:00
    Exposure Time [%]                   98.440926
    Equity Final [$]                  1002.619172
    Equity Peak [$]                   1006.984864
    Return [%]                           0.261917
    Buy & Hold Return [%]               -2.208577
    Return (Ann.) [%]                    1.221519
    Volatility (Ann.) [%]                6.575708
    Sharpe Ratio                         0.185762
    Sortino Ratio                        0.317436
    Calmar Ratio                           0.2837
    Max. Drawdown [%]                   -4.305667
    Avg. Drawdown [%]                   -0.614941
    Max. Drawdown Duration       45 days 06:05:00
    Avg. Drawdown Duration        5 days 12:43:00
    # Trades                                 1268
    Win Rate [%]                        71.214511
    Best Trade [%]                       0.498107
    Worst Trade [%]                     -0.908333
    Avg. Trade [%]                       0.002879
    Max. Trade Duration          10 days 23:35:00
    Avg. Trade Duration           2 days 05:23:00
    Profit Factor                         1.01897
    Expectancy [%]                       0.003978
    SQN                                  0.288167
    _strategy                           GridHedge
    _equity_curve                             ...
    _trades                         Size  Entr...
    dtype: object
    ```
* RSI Long
  <br/>To be continued...

### TODOS:
- [x] Fix venv Python 3.10+
- [x] Finish readme.md
- [ ] Finish correlation finders
- [ ] Add more trading Strategy and fix structure