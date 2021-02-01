# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

np.random.seed(10)

# %%
# url = ('https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/'
#       'dash_course/data.csv')
# df_raw = pd.read_csv(url, index_col=0)

# musialem sciezke absolutna bo byl blad dla "data.csv"
df_raw = pd.read_csv("/home/dell/PycharmProjects/dash-tut/08_case_studies_2/data.csv", index_col=0)
# %%
cols = ['Year', 'Fuel_Type', 'Transmission', 'Engine', 'Power', 'Seats', 'Price']

df = df_raw.copy()
df = df[cols]

# %%
# bierze tylko liczby a odrzuca CC. Ale nadal Engin to kolumna tekstowa
df.Engine = df.Engine.str.split(' ').str[0]
# bierze tylko liczby a odrzuca bhp. Ale nadal Engin to kolumna tekstowa
# zamienia strin "null" na np.nan
df.Power = df.Power.str.split(' ').str[0].replace('null', np.nan)

# %%
df.info()
# %%
df.isnull().sum()
# %%
df = df.dropna()

# %%
# z object na liczbowe
df.Engine = df.Engine.astype('float32')
df.Power = df.Power.astype('float32')

# %%
# rozklad rodzaju paliwa
df.Fuel_Type.value_counts()

# %%
# rozklad rodzaj skrzyni biegow
df.Transmission.value_counts()
# %%
df = pd.get_dummies(df, drop_first=True)
# %%
# musialem sciezke absolutna bo byl blad dla
# './datasets/data_cleaned.csv'
df.to_csv('/home/dell/PycharmProjects/dash-tut/08_case_studies_2/datasets/data_cleaned.csv')

# %%
X = df.copy()
y = X.pop('Price')

# %%
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y)

# %%
from sklearn.ensemble import RandomForestRegressor

reg = RandomForestRegressor()
reg.fit(X_train, y_train)

# wspolczynnik R kwadrat
reg_score = reg.score(X_test, y_test)
print(reg_score)

# %%
from sklearn.model_selection import GridSearchCV

param_grid = [{'max_depth': [3, 4, 5, 6, 7, 8, 10, 20],
               'min_samples_leaf': [3, 4, 5, 10, 15]}]

model = RandomForestRegressor()
# metoda oceny to R kwadrat
gs = GridSearchCV(model, param_grid=param_grid, scoring='r2')
gs.fit(X_train, y_train)

# %%
gs_score = gs.score(X_test, y_test)
print("gs_score", gs_score)
# %%
model = gs.best_estimator_

# %%
import pickle

# zapisuje model do pliku
# wb to write binary
with open('/home/dell/PycharmProjects/dash-tut/08_case_studies_2/model.pickle', 'wb') as file:
    pickle.dump(model, file)

