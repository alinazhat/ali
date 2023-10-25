# Import the requered libraries
# -------------------------------------
import requests # To make requests
import lxml # To parse HTML data
import csv # To save data into CSV file
import os 
from random import choice
requests.timeout = 5

# The web scraper
# -------------------------------------
def main():
    import requests

    headers = {
        'authority': 'prod-search-api.jobsyn.org',
        'accept': 'application/json',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8,fr;q=0.7,fr-FR;q=0.6,en-GB;q=0.5',
        'origin': 'https://usnlx.com',
        'referer': 'https://usnlx.com/',
        'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
        'x-origin': 'usnlx.com',
    }

    params = {
        'page': '1',
        'offset': '15',
        'num_items': '15',
    }

    response = requests.get('https://prod-search-api.jobsyn.org/api/v1/solr/search', params=params, headers=headers)
    print(response.json())


if __name__== "__main__":
    main()
