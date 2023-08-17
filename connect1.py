import pandas as pd
import pymysql as py
from sqlalchemy import create_engine
en=create_engine('mysql+pymysql://root:root@localhost:3306/mysql')
df=pd.read_sql_query('SELECT * FROM std1',en)
print(df)
