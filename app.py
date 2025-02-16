import pandas as pd
import plotly.express as px
import yfinance as yf
import streamlit as st
from model import coins, selic


btc = coins.makeCoinData('BTC-USD', 'max')
eth = coins.makeCoinData('ETH-USD', 'max')
sol = coins.makeCoinData('SOL-USD', 'max')


def makePlotCripto(db, title, lineColor='Orange', tileColor = 'Gray'):
  start_date = st.date_input('Informe a data inicial', value= db['date'].min(), min_value = db['date'].min(), max_value= db['date'].max())
  end_date = st.date_input('Informe a data Final', value= db['date'].mean(), min_value = db['date'].min(), max_value= db['date'].max())
  
  fig = px.line(db[(db['date'] >= pd.to_datetime(start_date)) & (db['date'] <= pd.to_datetime(end_date))], x='date', y='real_value', title= title)
  fig.update_traces(line=dict(color= lineColor))
  
  fig.update_layout(
    xaxis_title='Tempo',
    yaxis_title=f'Valores em R$',
    title_font=dict(size=24, family='Arial', color='Gray'),
    margin=dict(l=40, r=40, t=60, b=40),)
  st.plotly_chart(fig)

def makeSelicPlot(db):
 st.header('Selic')
 start_date = st.date_input('Informe a data inicial', value= pd.to_datetime(db['year-month'].min()))
 end_date = st.date_input('Informe a data Final', value= pd.to_datetime(db['year-month'].max()))
 
 fig = px.line(db[(pd.to_datetime(db['year-month']) >= pd.to_datetime(start_date)) & (pd.to_datetime(db['year-month']) <= pd.to_datetime(end_date))],
    x='year-month',
    y='month_selic',
    markers=True,
    title='Porcentagem da Selic ao Longo dos meses dos Anos'
)
 fig.update_layout(
    xaxis=dict(
        title_text='',
        showgrid=True,
        gridcolor='gray',
    ),
    yaxis=dict(
        title_text= 'Porcetagem da Selic',
        showgrid=True,
        gridcolor='gray'
    ),
 )

 fig.update_traces(
    hovertemplate='<b>%{x}</b><br>Porcetagem: %{y:.2f}%<extra></extra>'
 )
 st.plotly_chart(fig)



st.set_page_config(layout="wide")

coinsContainer = st.container()
selicContainer = st.container()

with coinsContainer:
  btcCol, ethCol, solCol = st.columns(3)
  with btcCol:
    st.image("https://cryptologos.cc/logos/bitcoin-btc-logo.png", width=100)
    makePlotCripto(btc, 'Valores do Bitcoin')
  with ethCol:
    st.image("https://cryptologos.cc/logos/ethereum-eth-logo.png", width=100)
    makePlotCripto(eth, 'Valores do Ethereum', '#3C3C3D')
  with solCol:
   st.image("https://cryptologos.cc/logos/solana-sol-logo.png", width=100)
   makePlotCripto(sol, 'Valores SOL', '#9945FF')

with selicContainer:
  makeSelicPlot(selic.make_selic_month_income())
  
