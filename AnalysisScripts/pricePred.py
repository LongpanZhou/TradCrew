import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_ta as ta
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Stock.Stock import Stock


import tensorflow as tf
import keras
from keras.layers import *
from keras.models import Sequential, Model
from keras import optimizers
from keras.callbacks import History

def pricePred(s: Stock, years):
    #download data
    data = yf.download(tickers=s.ticker, period=f'{years}y')

    #add indicators to data
    data['RSI'] = ta.rsi(data.Close, length=15)
    data['EMAF'] = ta.ema(data.Close, length=20)
    data['EMAM']=ta.ema(data.Close, length=100)
    data['EMAS']=ta.ema(data.Close, length=150)

    #add target values to data
    data['Target'] = data['Adj Close']-data.Open
    data['Target'] = data['Target'].shift(-1)
    data['TargetClass'] = [1 if data.Target[i]>0 else 0 for i in range(len(data))]
    data['TargetNextClose'] = data['Adj Close'].shift(-1)

    #drop useless columns
    data.dropna(inplace=True)
    data.reset_index(inplace=True)
    data.drop(['Volume','Close','Date'], axis=1, inplace=True)

    data_set = data.iloc[:,0:11]

    #re-scale data to 0-1
    sc = MinMaxScaler(feature_range=(0,1))
    data_set_scaled = sc.fit_transform(data_set)

    X = []
    backcandles = 15

    #append data to list
    for i in range(8):
        X.append([])
        for j in range(backcandles, data_set_scaled.shape[0]):
            X[i].append(data_set_scaled[j-backcandles:j,i])

    #move axis
    X = np.moveaxis(X, [0], [2])
    #Input Values
    X, Yi = np.array(X), np.array(data_set_scaled[backcandles:,-1])
    #Target Values
    Y = np.reshape(Yi,(len(Yi),1))

    #split data into train and test
    n = int(len(X)*0.8)
    X_train, X_test, X_final = X, X, X[len(X)-1:]
    Y_train, Y_test, Y_final = Y, Y, Y[len(Y)-1:]

    #Setting up neural network
    np.random.seed(10)

    lstm_input = Input(shape=(backcandles, 8), name='lstm_input')
    inputs = LSTM(150, name='first_layer')(lstm_input)
    inputs = Dense(1, name='dense_layer')(inputs)
    output = Activation('linear', name='output')(inputs)
    model = Model(inputs=lstm_input, outputs=output)
    adam = optimizers.Adam()
    model.compile(optimizer=adam, loss='mse')
    model.fit(x=X_train, y=Y_train, batch_size=15, epochs=30, shuffle=True, validation_split = 0.1)

    #Test Prediction
    Y_pred = model.predict(X_test)
    Y_final_pred = model.predict(X_final)

    # Inverse transform the scaled data to get back the original values
    avg_shift = (np.sum(Y_pred) - np.sum(Y_test))/len(Y_pred)
    Y_final_pred = np.repeat(Y_final_pred-avg_shift, 11, axis=1)
    Y_final_pred = sc.inverse_transform(Y_final_pred)

    print(f'The prediction for the next day is: {Y_final_pred[0][0]}$')

    #Plot
    plt.figure(figsize=(16,8))
    plt.plot(Y_test, label='Actual')
    plt.plot(Y_pred, label='Prediction')
    plt.legend()
    plt.show()

AAPL = Stock("AAPL")
pricePred(AAPL, 10)