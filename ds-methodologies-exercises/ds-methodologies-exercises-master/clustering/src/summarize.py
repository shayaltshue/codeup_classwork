import pandas as pd

def print_data_summary(df):
    '''
    Prints out summary statistics:
    - Shape
    - Info
    '''
    
    print(f'''Shape:
    Number of Rows: {df.shape[0]}
    Number of Columns: {df.shape[1]}
    -------------------------------------------------
    
    Info:
    {df.info()}
    ''')

def find_missing_rows(df):
    missing_rows = pd.DataFrame(
        {'num_rows_missing': df.isnull().sum(), 
         'pct_rows_missing': df.isna().sum() / len(df)
        },
        index=df.columns)
    
    return missing_rows

def find_missing_cols(df):
    missing_cols = pd.DataFrame(
        {'num_cols_missing': df.isna().sum(axis=1), 
         'pct_cols_missing': df.isna().sum(axis=1) / len(df)
        })
    
    return missing_cols