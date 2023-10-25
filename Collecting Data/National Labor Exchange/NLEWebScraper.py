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
    url = "https://prod-search-api.jobsyn.org/api/v1/solr/search"
    headers = staticHeaderRotator()  

def staticUserAgentRotator():
        user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/15.4 Safari/537.75.14",
        "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/15.4 Safari/537.75.14",
        "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/15.4 Safari/537.75.14",
        "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        ]
        return {'User-Agent': choice(user_agents)}

def staticHeaderRotator():
    headers = [
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'sec-ch-ua': 'Microsoft Edge;v="87", "Chromium";v="87", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'Windows', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip, deflate', 'accept-language': 'en-US,en;q=0.9,es;q=0.5'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'sec-ch-ua': 'Google Chrome;v="89", "Chromium";v="89", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'macOS', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip, deflate', 'accept-language': 'en-US,fr;q=0.5'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'sec-ch-ua': 'Google Chrome;v="90", "Chromium";v="90", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'macOS', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip', 'accept-language': 'en-US,es;q=0.8'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'sec-ch-ua': 'Google Chrome;v="84", "Chromium";v="84", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'Windows', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip, deflate', 'accept-language': 'en-US,en;q=0.9,fr;q=0.8'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'sec-ch-ua': 'Google Chrome;v="84", "Chromium";v="84", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'macOS', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip', 'accept-language': 'en-US,en;q=0.9,fr;q=0.8'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'sec-ch-ua': 'Google Chrome;v="84", "Chromium";v="84", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'Windows', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip', 'accept-language': 'en-US,en;q=0.7'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'sec-ch-ua': 'Google Chrome;v="83", "Chromium";v="83", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'macOS', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip', 'accept-language': 'en-US,en;q=0.9,es;q=0.8'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'sec-ch-ua': 'Microsoft Edge;v="87", "Chromium";v="87", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'Windows', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip', 'accept-language': 'en'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'sec-ch-ua': 'Google Chrome;v="89", "Chromium";v="89", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'Windows', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip, deflate', 'accept-language': 'en'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'sec-ch-ua': 'Google Chrome;v="86", "Chromium";v="86", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'macOS', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip', 'accept-language': 'en-US,it;q=0.7'}
        ]
    return choice(headers)

def apiheadersRotator():
    response = requests.get('https://headers.scrapeops.io/v1/browser-headers',params={'api_key': 'fba52e3f-8ad2-4af3-a04c-e2f567f1fe8e','num_headers': '10'})
    headers = response.json()['result']
    return choice(headers)

if __name__== "__main__":
    main()
