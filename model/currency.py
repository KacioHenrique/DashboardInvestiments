import pandas as pd
from bcb import currency

today = (pd.to_datetime('today') + pd.Timedelta(days=1)).strftime("%Y-%m-%d")

dbConvertDollar = currency.get(['USD'],
                  start='2000-01-01',
                  end= today,
                  side='ask').reset_index()


def dolar_to_real(date, value):
  return dbConvertDollar[dbConvertDollar['Date'] <= date.date().strftime("%Y-%m-%d")]['USD'].values[-1].round(2) * value
