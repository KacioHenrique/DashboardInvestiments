from model import currency
import yfinance as yf
import pandas as pd

def makeCoinData(ticker, period):
  db = yf.download(tickers= ticker, period= period).reset_index()
  data = {'date': db['Date'].tolist(), 'value': db['Close'][ticker].to_list()}
  generate_db = pd.DataFrame(data)
  generate_db['real_value'] = generate_db[['date', 'value']].apply(lambda x: currency.dolar_to_real(x['date'], x['value']), axis=1)
  return generate_db
