import pandas as pd
import numpy as np

def get_logs():
    colnames=['date', 'timestamp', 'request_method', 'user_id', 'cohort', 'ip']

    df = pd.read_csv('curriculum-access.txt',          
                     engine='python',
                     header=None,
                     index_col=False,
                     names=colnames,
                     sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
                     na_values='"-"')
                     
    df['date_time'] = df.date + ' ' + df.timestamp
                     
    df.drop(columns=['date', 'timestamp'], inplace=True)
    
    df.date_time = pd.to_datetime(df.date_time)
                     
    df.set_index('date_time', inplace=True)
    
    return df