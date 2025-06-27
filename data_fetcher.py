from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()

REQUEST_URL = "http://www.omdbapi.com/?"

API_KEY = os.getenv("API_KEY")


def fetch_data(title):
    """Fetching movie data from API"""
    data = requests.get(REQUEST_URL + 'apikey=' + API_KEY + '&t=' + title)
    if data.status_code != 200:
        print(f"Error fetching data. Status code: {data.status_code}")
        return None
    elif data.json()['Response'] == 'False':
        print(f"Error fetching data. Error: {data.json()['Error']}")
        return None
    else:
        return data.json()
