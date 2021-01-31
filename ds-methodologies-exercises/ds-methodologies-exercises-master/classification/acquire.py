from env import get_url_for_pancakes

import pandas as pd

def get_titanic_data():
    query = '''
    SELECT *
    From passengers
    '''
    
    titanic_url = get_url_for_pancakes('titanic_db')
    
    return pd.read_sql(query, titanic_url)
    
    
def get_iris_data():
    query = '''
    SELECT *
    From measurements
    JOIN species USING(`species_id`)
    '''
    
    iris_url = get_url_for_pancakes('iris_db')
    
    return pd.read_sql(query, iris_url)
    
    