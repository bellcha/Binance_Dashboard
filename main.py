from git import refresh
import streamlit as st
import pandas as pd
from mysql.connector import MySQLConnection, Error
from mysql_config import read_config

def btc_histroy():
    db_config = read_config()

    conn = MySQLConnection(**db_config)

    sql_query = pd.read_sql_query ('''SELECT * FROM btchistory ORDER BY date DESC''', conn)

    df = pd.DataFrame(sql_query, columns = ['date', 'side', 'price', 'qty', 'quoteQty'])

    return df

def itoa_history():
    db_config = read_config()

    conn = MySQLConnection(**db_config)

    sql_query = pd.read_sql_query ('''SELECT * FROM iotahistory ORDER BY date DESC''', conn)

    df = pd.DataFrame(sql_query, columns = ['date', 'side', 'price', 'qty', 'quoteQty'])

    return df

def eth_history():

    db_config = read_config()

    conn = MySQLConnection(**db_config)

    sql_query = pd.read_sql_query ('''SELECT * FROM ethhistory ORDER BY date DESC''', conn)

    df = pd.DataFrame(sql_query, columns = ['date', 'side', 'price', 'qty', 'quoteQty'])

    return df


st.title('Binance Trade History')

coin = st.selectbox('Choose a coin', ('BTC', 'IOTA', 'ETH'))


if 'number of rows' not in st.session_state:
    st.session_state['number of rows'] = 5

increment = st.button('Show more history ⬆️')

if increment:
    st.session_state['number of rows'] += 1

decrement = st.button('Show less history ⬇️')

if decrement:
    st.session_state['number of rows'] -= 1

if coin == 'BTC':
    trades = btc_histroy()

if coin == 'IOTA':
    trades = itoa_history()

if coin == 'ETH':
    trades = eth_history()

st.table(trades.head(st.session_state['number of rows']))