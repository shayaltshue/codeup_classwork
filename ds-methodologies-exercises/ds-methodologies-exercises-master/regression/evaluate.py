import pandas as pd
import numpy as np

from statsmodels.formula.api import ols
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import explained_variance_score as evs

from math import sqrt

def plot_residuals(actual, predicted, df):
        sns.relplot(x=actual, y=predicted, data=df)

def regression_errors(actual, predicted):
    '''
    Takes:
        actual - df.series: actual values of the y
        predicted - df.series: model's prediction of the y values
    Returns:
        Sum of Squared Errors (SSE)
        Evaluated Sum of Squares (ESS)
        Total Sum of Squares (TSS)
        Mean Squared Error (MSE)
        Root Mean Squared Error (RMSE)
    '''
    SSE = mse(actual, predicted) * len(actual)
    ESS = sum((predicted - actual.mean()) **2)
    TSS = ESS + SSE
    MSE = mse(actual, predicted)
    RMSE = sqrt(MSE)

    return SSE, ESS, TSS, MSE, RMSE

def baseline_mean_errors(actual, predicted_baseline):
    '''
    Takes in the actual values for y and the predicted baseline values for y.
    Returns the SSE, MSE and RMSE for the baseline.
    '''
    SSE_bl = mse(actual, predicted_baseline) * len(actual)
    MSE_bl = mse(actual, predicted_baseline)
    RMSE_bl = sqrt(MSE_bl)

    return SSE_bl, MSE_bl, RMSE_bl

def better_than_baseline(RMSE, RMSE_baseline) -> None:
    '''
    Takes in the RMSE for a model as well as the RMSE for the baseline and compares the two.
    Prints out if the model is better or worse than the baseline.
    '''
    if RMSE < RMSE_baseline:
         print('Model is better than baseline')
    else: 
        print('Model sucks, should have done full stack dev instead.')

def model_significance(model, actual, predicted):
    '''
    Takes in a model, the actual y values, and the predicted y values.
    Calculates the significance of the model by comparing it's p value to an alpha of 0.05.
    Prints out whether or not the model is significant.
    Returns the Explained Variance of Squares.
    '''
    p = model.f_pvalue
    alpha = 0.05
ß
    EVS = evs(actual, predicted)

    if p < 0.05:
        print(f'p: {p} is less than alpha: {alpha}, therefore our model is significant.')
    else:
        print(f'p: {p} is greather than alpha: {alpha}, therefore our model is not significant.')

    print('\n')
    print(f"EVS: {EVS}")
    
    return evs