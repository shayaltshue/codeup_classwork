import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

def train_test_val_split(train_size, test_size, val_size, df, seed):
    train, val = train_test_split(train_size=train_size, test_size=val_size, data=df, random_state=seed)
    train, test = train_test_split(train_size=train_size, test_size=test_size, data=df, random_state=seed)
    return train, test, val

def model_and_predict(train, x_values, y_value):
    # Create and fit the model
    log_reg = LogisticRegression().fit(train[x_values])

    # Create a predictions dataframe
    predictions = pd.DataFrame({'actual': train[y_value]})

    # Use model to create predictions
    predictions['model_predictions'] = log_reg.predict(train[x_values])

    return predictions, log_reg

def create_log_reg_model(df, train_size, test_size, val_size, x_values, y_value, seed):
    '''
    Takes in the following:
    - train: DataFrame with the train information
    - test: Da
    - x_values: list of features which will be used as predictors
    - y_values: thing to be predicted
    
    Returns:
    - train, test, val (3 seperate dataframes)
    - predictions: dataframe containing the actual vs model predictions
    - log_reg: the model
    '''


    # 2. Create the model and predictions dataframe
    predictions, log_reg = model_and_predict(train, x_values, y_value)

    return train, test, val, predictions, log_reg