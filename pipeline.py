# pipeline.py
import os
import logging
import requests
import pandas as pd
from config import API_URL, OUTPUT_PATH

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('todos_pipeline')


def fetch_data(url):
    logger.info(f"Fetching from {url}")
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def clean_data(records):
    logger.info(f"Cleaning {len(records)} records")
    df = pd.DataFrame(records)
    df = df[df['completed'] == True]
    return df


def save_data(df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_parquet(path)
    logger.info(f"Saved {len(df)} records to {path}")


def run():
    try:
        records = fetch_data(API_URL)
        df = clean_data(records)
        save_data(df, OUTPUT_PATH)
        logger.info("Pipeline complete")
    except Exception as e:
        logger.critical(f"Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    run()