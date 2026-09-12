import pandas as pd

from sqlalchemy import create_engine, URL
from dotenv import load_dotenv
import os

load_dotenv()

input_file = "data/cleaned_earthquake_data_2021_2025.csv"

df = pd.read_csv(input_file)

print("Dataset loaded successfully")
print("Shape:", df.shape)

username = "root"
password = os.getenv("MYSQL_PASSWORD")
host = "localhost"
port = 3306
database = "global_seismic_db"

connection_url = URL.create(
    drivername="mysql+pymysql",
    username=username,
    password=password,
    host=host,
    port=port,
    database=database
)

engine = create_engine(connection_url)

print("Connecting to MySQL...")

df.to_sql(
    "earthquakes",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data uploaded successfully!")

check_df = pd.read_sql(
    "SELECT COUNT(*) AS total_records FROM earthquakes",
    engine
)

print()
print("Records in MySQL:")
print(check_df)

engine.dispose()

print()
print("MySQL connection closed.")