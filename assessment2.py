import os
import re
import datetime
import requests
import sqlalchemy
import pandas as pd

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_USERNAME=os.getenv("MYSQL_USER")
DB_PASSWORD=os.getenv("MYSQL_PASSWORD")
DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_NAME=os.getenv("DB_NAME")

def scrape_exchange_rate():
    url ="https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=IDR"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    rate_tag = soup.find("p", class_="sc-e08d6cef-1 fwpLse")
    rate = rate_tag.text.strip() if rate_tag else None
    rate = re.sub(r"[^0-9,\.]", "", rate)
    print("rate: "+ str(rate))
    if rate:
        return float(rate.replace(',', ''))
    else:
        raise Exception("Failed to scrape exchange rate data.")

def process_data(rate):
    data = {
    'date': [datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
    'usd_to_idr': [rate]
    }
    df = pd.DataFrame(data)
    return df

def ingest_data(df, db_engine):
    table_name = 'exchange_rate_usd_idr'
    print("Ingest data")
    df.to_sql(table_name, con=db_engine, if_exists='append', index=False)
    print(f"Data ingested into {table_name} table successfully.")
    
def main():
    try:
        exchange_rate = scrape_exchange_rate()
        print(f"Exchange Rate (USD to IDR): {exchange_rate}")

        data_frame = process_data(exchange_rate)
        db_url =f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
        engine = create_engine(db_url)

        ingest_data(data_frame, engine)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

