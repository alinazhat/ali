# Import the requered libraries
# -------------------------------------
import requests # To make requests
from bs4 import BeautifulSoup
import lxml # To parse HTML data
import csv # To save data into CSV file
import os 
from random import choice
requests.Timeout = 120

# The web scraper
# -------------------------------------
def main():
    url = "https://www.dice.com/jobs/q--jobs?p=" # The job search first page URL
    headers = staticHeadersRotator()
    offset, positions, pages = get_website_structure(url, headers=headers)
    print('offset:', offset)
    print('positions:', positions)
    print('pages:', pages)
    for i, page in enumerate(range(pages),1): # Loob through every page
        print(f'Page: {i}')
        print(f'    {offset*(i-1)} jobs data collected so far.')
        while True: # Keep looping
            try: # Try to reqeust a page
                mainReponce = requests.get(f"https://www.dice.com/jobs/q--jobs?p={str(page+1)}", headers=headers)
                mainSoup = BeautifulSoup(mainReponce.text, 'lxml')
                mainData = mainSoup.find_all('a', class_="dice-btn-link loggedInVisited easy-apply")
                print("    Page request Succeed ")
                break # Until the the requeset secceed
            except: # Otherwise 
                print("    Page request failled")
                headers = staticHeadersRotator() # Change the request headers 
                continue # And Loob again

        for n, datum in enumerate(mainData, 1): # Loop trough every job post in the current page
                print(f"    Job: {n}")
                while True: # Keep looping
                    try: # Try to request a job
                        subResponce = requests.get(f'https://www.dice.com{datum["href"]}', headers=headers)
                        subSoup = BeautifulSoup(subResponce.text, 'lxml')
                        print("         Job request succeed")
                        break # Untill the request succeed
                    except: # Otherwese
                        headers = staticHeadersRotator() # Change the request headers
                        print("         Job request failled")
                        continue # And Loop Again

                id = str((i-1)*20 + n)
                # Try to get the job information, return None values otherwise    
                try:
                    title = subSoup.find('h1', {"data-cy":"jobTitle"}).text
                except:
                    title = None
                    
                try:
                    skills = [skill.text for skill in subSoup.find('ul', {"data-cy":"skillsList"})]
                except:
                    skills = []
                
                try:
                    companyName = subSoup.find('a', {"data-cy":"companyNameLink"}).text
                except:
                    companyName = None
                    
                try:
                    employmentType = subSoup.find('p', {"data-cy":"employmentType"}).text
                except:
                    employmentType = None
                    
                try:
                    salary = subSoup.find('p', {"data-cy":"compensationText"}).get_text()
                except:
                    salary = None
                    
                try:
                    remote = subSoup.find('p', {"data-cy":"workFromHome"}).text
                except:
                    remote = None
                    
                try:
                    companyLocation = subSoup.find('li', {"data-cy":"companyLocation", "data-testid":"companyLocation"}).text
                except:
                    companyLocation = None
                    
                try:
                    description = subSoup.find('div', {"data-testid":"jobDescriptionHtml"}).text
                except:
                    description = None
                    
                try:
                    postedDate = subSoup.find('dhi-time-ago')['posted-date']
                except:
                    postedDate = None
                    
                try:
                    updatedDate = subSoup.find('dhi-time-ago')['modified-date']
                except:
                    updatedDate = None
                    
                try:
                    positionId = subSoup.find('li', {"data-testid":"legalInfo-referenceCode"}).text.split(' ')[-1]
                except:
                    positionId = None
                    
                try:
                    companyId = subSoup.find('li', {"data-testid":"legalInfo-companyName"}).text.split(' ')[-1]
                except:
                    companyId = None
                print("         Seccess scraping")    

def get_website_structure(url, headers):
    '''This function purpose is to get the sturcture of the page, it returns:
        1. offset: indicates how many items to skip from the beginning, number of items in every page(for the first page)
        2. allPositions: count of all positions
        3. allPages: Number of pages '''
    while True: # keep looping
        try: # Request for page sturcture
            responce = requests.get(url, headers=headers)
            if responce.status_code !=200: # If request not succeed
                print('Structure reqeust failled')
                headers = staticHeadersRotator() # Change the request headers
                continue # Retry
            print("Sturcture request succeed")
            break # Break otherwise
        except: # If error happens (timeout error for instanse)
            print('Structure reqeust failled')
            headers = staticHeadersRotator() # Change the request headers
            continue # And Loop Again
    soup = BeautifulSoup(responce.text, 'lxml')
    data = soup.find('div', class_="col-md-12 col-lg-12")
    offset = int(data.find('span').text.split(' ')[-1])
    data = soup.find('span', id="posiCountId")
    allPositions = int(data.text.replace(',',''))
    allPages = int(allPositions/offset+1)
    return (offset, allPositions, allPages)

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

def staticHeadersRotator():
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