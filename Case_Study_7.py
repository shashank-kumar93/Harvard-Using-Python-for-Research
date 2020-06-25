import pandas as pd
import numpy as np

from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt

df = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@movie_data.csv", index_col=0)

#Exercise 1

print (df['title'].head())

#Exercise 2

df['profitable'] =  np.where(df.revenue > df.budget, 1, 0)
no_of_profitable = df[df.profitable == 1].shape[0]

regression_target = 'revenue'
classification_target = 'profitable'


#Exercise 3

df = df.replace([np.inf, -np.inf], np.nan)
df.dropna(axis=0,inplace=True)
print(df.shape[0])


#Exercise 4

list_genres = df.genres.apply(lambda x: x.split(","))
genres = []
for row in list_genres:
    row = [genre.strip() for genre in row]
    for genre in row:
        if genre not in genres:
            genres.append(genre)
for genre in genres:
    df[genre] = df['genres'].str.contains(genre).astype(int)

print(df[genres].shape)

#Exercise 5

continuous_covariates = ['budget', 'popularity', 'runtime', 'vote_count', 'vote_average']
outcomes_and_continuous_covariates = continuous_covariates + [regression_target, classification_target]
plotting_variables = ['budget', 'popularity', regression_target]

axes = pd.plotting.scatter_matrix(df[plotting_variables], alpha=0.15, color=(0,0,0), hist_kwds={"color":(0,0,0)}, facecolor=(1,0,0))
plt.show()
print(df[outcomes_and_continuous_covariates].skew())

#Exercise 6

variables = ['budget', 'popularity', 'runtime', 'vote_count', 'revenue']
for covariate in variables:
    df[covariate] = df[covariate].apply(lambda x: np.log10(1+x))
    
print(df[outcomes_and_continuous_covariates].skew())

#Exercise 7
df.to_csv("movies_clean.csv")

