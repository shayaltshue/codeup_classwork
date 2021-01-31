import pandas as pd

import sklearn.preprocessing
    
def drop_columns(df):
    return df.drop(columns=['species_id', 'measurement_id'])

def rename_columns(df):
    return df.rename(columns={'species_name': 'species'})

def make_new_columns(df):
    df['sepal_area'] = df.sepal_length * df.sepal_width
    df['petal_area'] = df.petal_length * df.petal_width
    return df

def encode_column(df):
    encoder = sklearn.preprocessing.LabelEncoder().fit(df.species)
    df['encoded'] = encoder.transform(df.species)
    return df

def prep_iris(raw_data):
    #1. Drop columns
    df = drop_columns(raw_data)
    #2. Rename columns
    df = rename_columns(df)
    #4. Add new columns
    df = make_new_columns(df)
    #4. Encode columns
    df = encode_column(df)
    
    return df

def prep_titanic(df):
    # 1. Drop Columns
    df.drop(columns='deck', inplace=True)
    
    # 2. Handling Missing Values
    df.embark_town.fillna('Southampton', inplace=True)
    df.embarked = df.embarked.fillna('S')
    df.age.fillna(df.age.median(), inplace=True)
    
    # 3. Encode
    encoder_embarked = sklearn.preprocessing.LabelEncoder()
    encoder_sex      = sklearn.preprocessing.LabelEncoder()
    df.embarked = encoder_embarked.fit_transform(df[['embarked']])
    df.sex      = encoder_sex.fit_transform(df[['sex']])
    
    encoder = sklearn.preprocessing.OneHotEncoder(sparse=False, categories='auto')
    matrix = encoder.fit_transform(df[['embark_town']])
    embark = pd.DataFrame(matrix, columns=encoder.categories_[0], index=df.index)
    df = df.join(embark)
    
    return df