import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse

engine = create_engine('postgresql://root:root@localhost:5432/de_test')
engine.connect()
df_iter = pd.read_csv('docker/yellow_tripdata_2021-07.csv', iterator = True, chunksize = 100000)
df = next(df_iter)

df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

df.to_sql(name='yellow_taxi_data', con=engine ,if_exists='append')