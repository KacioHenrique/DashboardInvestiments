import pandas as pd
from bcb import sgs


selicDb = sgs.get({'selic':432}, start='2016-03-05').reset_index()

def date_to_month(db):
  months = range(db['Date'].dt.month.min() , db['Date'].dt.month.max())
  years = range(db['Date'].dt.year.min(), db['Date'].dt.year.max() + 1)
  maxDate = db['Date'].max()
  result = []
  for year in years:
    for month in months:
      if year == maxDate.year and month > maxDate.month:
        break
      month_target = db[(db['Date'].dt.month == month) & (db['Date'].dt.year == year)]
      month_mean = month_target['selic'].mean()
      result.append({'year-month': f'{year}-{month}', 'month_selic': month_mean})

  return pd.DataFrame(data= result, columns= ['year-month','month_selic'])


def make_selic_month_income():
    selic_month_icome = date_to_month(selicDb)    
    return selic_month_icome
