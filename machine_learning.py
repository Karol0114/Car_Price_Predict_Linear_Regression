import analysis as an
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import functions as fn


# Podział danych na dane treingowe i testowe

X_train, X_test, y_train, y_test = train_test_split(
    an.df_copy.drop(columns = ['prices_log']),
    an.df_copy['prices_log'],
    test_size = 0.3,
    random_state= 123
    )


#Regresja liniowa:

model = LinearRegression()

#Trening modelu:

model.fit(X_train, y_train)

#Predykcje dla danych treningowych:

pred_train = model.predict(X_train)

plt. figure()
plt.scatter(list(range(len(y_train))), y_train)
plt.scatter(list(range(len(pred_train))), pred_train)
plt.legend(['real', 'pred'])
plt.title('Dane treningowe')

plt.show()

#Błedy:

fn.linear_regression_errors(y_train, pred_train, 'train')


# Predykcje dla danych testowych:


pred_test = model.predict(X_test)

plt. figure()
plt.scatter(list(range(len(y_test))), y_test)
plt.scatter(list(range(len(pred_test))), pred_test)
plt.legend(['real', 'pred'])
plt.title('Dane testowe')

plt.show()


fn.linear_regression_errors(y_test, pred_test, 'test')


# Na podstawie macierzy korelacji ograniczamy sie tylko do kolumn: horsepower, enginesize, curbweight, carwidth, carlength, citympg, highwaympg, wheelbase, boreratio

X_train_sel = X_train[['horsepower', 'enginesize', 'curbweight', 'carwidth', 'carlength', 'citympg', 'highwaympg', 'wheelbase', 'boreratio']]
X_test_sel = X_test[['horsepower', 'enginesize', 'curbweight', 'carwidth', 'carlength', 'citympg', 'highwaympg', 'wheelbase', 'boreratio']]

model_sel = LinearRegression()

#Trening modelu:
model_sel.fit(X_train_sel, y_train)

#Predykcje dla danych treningowych:
pred_train_sel = model_sel.predict(X_train_sel)

fn.linear_regression_errors(y_train, pred_train_sel, 'train')

##Ograniczenie danych wpływa na złożoność czasową modelu, natomiast trace na precyzji predykcji. W tym przypadku danych jest na tyle mało, że nie opłacalne jest redukowanie kolumn

## błąd r2 rzedu 0.95 jest świetnym wynikiem

