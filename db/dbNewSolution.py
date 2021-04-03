import sqlalchemy as db
from sqlalchemy.engine import URL
import pandas as pd
import yfinance as yf

# Windows Authentication
connection_string = "DRIVER={SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=test;TRUSTED_CONNECTION=yes"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

engine = db.create_engine(connection_url)

# grab some data
data = yf.download(tickers='AMAT',period='1y')
print(data)

# put yfinance data into a pandas dataframe **doesn't work for date!**
df = pd.DataFrame(data, columns=['Date','Open','High','Low','Close','Adj Close','Volume'])

# put the dataframe in your sql server
df.to_sql('AMAT',engine, if_exists='replace',index=False) 

#define the table you'll be working with, for use in query below
metadata = db.MetaData()
amat = db.Table('AMAT',metadata,autoload=True,autoload_with=engine)

# Equivalent to 'SELECT * FROM amat'
query = db.select([amat])

with engine.connect() as connection:
    resultProxy = connection.execute(query)
    result = resultProxy.fetchall()

df_new = pd.DataFrame(result)
df_new.columns = result[0].keys()
print(df_new)

