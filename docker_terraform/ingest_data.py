import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse
import os

def main(params):

   user = params.user
   password = params.password
   host = params.host
   port = params.port
   database = params.database
   table = params.table

   csv_name = 'yellow_tripdata_2021-07.csv'

   # os.system(f"wget {url} -o {csv_name}")
   
   #download the csv
   engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

   df_iter = pd.read_csv(csv_name, iterator = True, chunksize = 100000)
   df = next(df_iter)

   df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
   df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

   df.head(n=0).to_sql(name=table, con=engine ,if_exists='replace')

   while True:
      t_start = time()
      
      df = next(df_iter)
      
      df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
      df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
      
      df.to_sql(name=table, con=engine ,if_exists='append')
      
      t_end = time()
      
      print ('insert another chuk, took %.3f sechond' % (t_end - t_start))

if __name__ == '__main__':
   parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')
   parser.add_argument('--user', help="user name for postgres")
   parser.add_argument('--password', help="password name for postgres")
   parser.add_argument('--host', help="host name for postgres")
   parser.add_argument('--port', help="post name for postgres")
   parser.add_argument('--database', help="database name for postgres")
   parser.add_argument('--table', help="table name where we will write the result to")
   # parser.add_argument('--url', help="file path of the CSV file")

   args = parser.parse_args()
   main(args)