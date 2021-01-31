# Imports
import acquire
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

#---------- Sales ----------#

def wrangle_sales(sales):
    sales['sale_date'] = pd.to_datetime(sales['sale_date'])
    sales.set_index('sale_date', inplace=True)
    
    sales['month'] = sales.index.month_name()
    sales['day_of_week'] = sales.index.day_name()
    
    sales['sales_total'] = sales.sale_amount * sales.item_price
    sales['sales_diff'] = sales.sales_total.diff()
    
    return sales
    
def plot_distributions(sales):
    sales.sale_amount.hist()
    plt.title('Sales Amount Distribution')
    
    sales.item_price.hist()
    plt.title('Item Price Distribution')
    
#---------- German ----------#

def wrangle_german_data(ops):
    ops.rename(columns={'Date':'date',
                    'Consumption':'consumption',
                    'Wind':'wind', 
                    'Solar':'solar',
                    'Wind+Solar':'wind_and_solar'
                   }, inplace=True)
    ops['date'] = pd.to_datetime(ops['date'])
    ops.set_index('date', inplace=True)
    
    ops['month'] = ops.index.month_name()
    ops['year'] = ops.index.year

    return ops


#---------- SF Temp ----------#

def wrangle_sf_temp_data(sf_temp):
    sf_temps.set_index('date', inplace=True)
    
    sf_temps["daily_average"] = sf_temps.resample("D").mean()
    sf_temps['daily_min'] = sf_temps.temp.resample("D").min()
    sf_temps['daily_max'] = sf_temps.temp.resample("D").max()
    
    sf_temps = sf_temps.ffill()
    
    resampled_sf = sf_temps.resample('D').agg(['min', 'max'])
    
    return sf_temps, resampled_sf

def plot_sf(sf_temp, resampled_sf):
    sf_temps.plot()
    
    sf_temps.daily_min.plot()
    plt.title('Minimum Temperature on Average')
    
    sf_temps.daily_max.plot()
    plt.title('Maximum Temperature on Average')
    
    resampled_sf.plot()