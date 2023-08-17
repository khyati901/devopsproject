import pandas as pd
import pymysql as py
from sqlalchemy import create_engine
en=create_engine('mysql+pymysql://root:root@localhost:3306/world')
data={'Sid':[162,2,3,4,5],'Sname':['Tanu singh','Bangalore','Mumbai','Chandigarh','Kerala']}
df=pd.DataFrame(data)
df.to_sql('emp123',en,if_exists="replace",index=True)

print("data saved from python code to my sql database")

