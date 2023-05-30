import analysis as an
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


#Funkcja, która generuje błędy dla regresji liniowej, podajemy dane, predykcję oraz w data_type='' -> test lub train, w zależności od tego jakich danych używamy
def linear_regression_errors(y, pred, data_type = ''):
    if data_type == 'train':
        print(f"MSE error for train data: {mean_squared_error(np.exp(y), np.exp(pred))}")
        print(f"RMSE error for train data: {mean_squared_error(np.exp(y), np.exp(pred), squared=False)}")
        print(f"r2 score for train data: {r2_score(np.exp(y), np.exp(pred))}")
    elif data_type == 'test':
        print(f"MSE error for test data: {mean_squared_error(np.exp(y), np.exp(pred))}")
        print(f"RMSE error for test data: {mean_squared_error(np.exp(y), np.exp(pred), squared=False)}")
        print(f"r2 score for test data: {r2_score(np.exp(y), np.exp(pred))}")