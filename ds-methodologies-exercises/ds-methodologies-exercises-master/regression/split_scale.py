from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, QuantileTransformer, PowerTransformer, RobustScaler

import pandas as pd

def split_data(X, y, seed, train_pct):
    '''
    Takes in an X, y, seed, train_pct. Returns X_train, X_test, y_train, y_test.
    '''
    return train_test_split(X, y, random_state=seed, train_size=train_pct)

def std_scaler(train, test):
    scaler = StandardScaler()
    scaler.fit(train)
    train = pd.DataFrame(scaler.transform(train), columns=train.columns, index=train.index)
    test = pd.DataFrame(scaler.transform(test), columns=test.columns, index=test.index)
    return scaler, train, test

def inverse_scaler(scaler, train, test):
    train_unscaled = pd.DataFrame(scaler.inverse_transform(train), columns=train.columns.values).set_index([train.index.values])
    test_unscaled = pd.DataFrame(scaler.inverse_transform(test), columns=test.columns.values).set_index([test.index.values])
    return scaler, train_unscaled, test_unscaled

def uniform_scaler(train, test):
    scaler = QuantileTransformer()
    scaler.fit(train)
    train = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return scaler, train, test

def gaussian_scaler(train, test):
    scaler = PowerTransformer()
    scaler.fit(train)
    train = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return scaler, train, test    

def min_max_scaler(train, test):
    scaler = MinMaxScaler()
    scaler.fit(train)
    train = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return scaler, train, test    
    
def iqr_robust_scaler(train, test):
    scaler = RobustScaler()
    scaler.fit(train)
    train = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return scaler, train, test