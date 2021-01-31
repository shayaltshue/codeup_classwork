import wrangle
import split_scale

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

def plot_box(x, y):
    sns.boxplot(x, y)

def plot_bar(x, y):
    sns.barplot(x, y)

def plot_swarm(x, y):
    sns.swarmplot(x,y)

def plot_variable_pairs(df):
    with sns.axes_style('white'):
        g = sns.pairplot(data=df, kind='reg', height=5);
    plt.show()
    return g

def months_to_years(tenure_months, df):
    '''
    Takes in a series (tenure_months) and a dataframe, returns the dataframe with a new column with years the customer has been there as a continous variable.
    '''
    df['years_as_customer'] = round(tenure_months/12).astype(int)

def plot_categorical_and_continous_vars(cont_var, categorical_var):
    x = cont_var
    y = categorical_var

    sns.set(style='white', palette='muted', color_codes=True)
    f, axes = plt.subplots(3, 1, figsize=(16,16))

    sns.boxplot(x, y, ax=axes[0])
    sns.barplot(x, y, ax=axes[1])
    sns.swarmplot(x, y, ax=axes[2])
    
    def i_like_turtles():
        print('True')