import requests
import pandas as pd
from os.path import isfile

#---------- Sales Data ----------#
def get_items():
    response = requests.get('https://python.zach.lol/api/v1/items')
    items = response.json()

    data = items['payload']['items']
    for n in range(2, items['payload']['max_page'] + 1):
        response = requests.get('https://python.zach.lol/api/v1/items?page=' + str(n))
        items = response.json()
        data.extend(items['payload']['items'])

    return pd.DataFrame(data)


def get_stores():
    response = requests.get('https://python.zach.lol/api/v1/stores')
    stores = response.json()

    data = stores['payload']['stores']
    for n in range(2, stores['payload']['max_page'] + 1):
        response = requests.get('https://python.zach.lol/api/v1/stores?page=' + str(n))
        stores = response.json()
        data.extend(stores['payload']['stores'])

    return pd.DataFrame(data)
   

def get_sales():
    response = requests.get('https://python.zach.lol/api/v1/sales')
    sales = response.json()

    data = sales['payload']['sales']
    for n in range(2, sales['payload']['max_page'] + 1):
        response = requests.get('https://python.zach.lol/api/v1/sales?page=' + str(n))
        sales = response.json()
        data.extend(sales['payload']['sales'])

    return pd.DataFrame(data)


def make_csvs_items_stores_sales():
    # Get the data into dataframes
    items  = get_items()
    stores = get_stores()
    sales  = get_sales()
    
    # Save the dataframes to CSVs in the data folder
    items.to_csv('data/items.csv')
    stores.to_csv('data/stores.cvs')
    sales.to_csv('data/sales.csv')
    
    
def merge_stores_data():
    items = pd.read_csv('data/items')
    stores = pd.read_csv('data/stores')
    sales = pd.read_csv('data/sales')
    
    for df in [items, stores, sales]:
        df.drop(df.columns[0], axis=1, inplace=True)

    sales.rename(columns={'store': 'store_id', "item":'item_id'}, inplace=True)
    
    df = pd.merge(sales, items, on='item_id')
    df = pd.merge(df, stores, on='store_id')    
    
    return df
    
    
def get_all_store_data():
    return merge_stores_data()


#---------- Germany Data ----------#
def get_germany_data():
    return pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
 