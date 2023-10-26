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
    'offset': '15', # after some tries, I found the maximum is 10000
    'num_items': '15', 
}
    offset, positions, pages = get_website_structure(url, headers=headers, params=params)
    for page in range(1,positions/5000):
        params = {
        'page': str(page),
        'offset': 5000, # after some tries, I found the maximum is 10000
        'num_items': 5000, 
        }
        while True:
            try:
                response = requests.get(url=url, headers=headers, params=params)
                if response.status_code != 200:
                    print('request failed')
                    continue
                break
            except:
                continue
        
        data = response.json()
        for job in data['jobs']:
            try:
                GeoLocation = job['GeoLocation']
            except:
                GeoLocation = 'None'

            try:
                _version_ = job['_version_']
            except:
                _version_ = 'None'

            try:
                all_locations = job['all_locations']
            except:
                all_locations = 'None'

            try:
                buid = job['buid']
            except:
                buid = 'None'

            try:
                city_exact = job['city_exact']
            except:
                city_exact = 'None'

            try:
                city_slab_exact = job['city_slab_exact']
            except:
                city_slab_exact = 'None'

            try:
                company_buid_slab = job['company_buid_slab']
            except:
                company_buid_slab = 'None'

            try:
                company_buid_slab_exact = job['company_buid_slab_exact']
            except:
                company_buid_slab_exact = 'None'

            try:
                company_exact = job['company_exact']
            except:
                company_exact = 'None'

            try:
                company_member = job['company_member']
            except:
                company_member = 'None'

            try:
                company_slab_exact = job['company_slab_exact']
            except:
                company_slab_exact = 'None'

            try:
                country_ac = job['country_ac']
            except:
                country_ac = 'None'

            try:
                country_exact = job['country_exact']
            except:
                country_exact = 'None'

            try:
                country_short_exact = job['country_short_exact']
            except:
                country_short_exact = 'None'

            try:
                country_slab_exact = job['country_slab_exact']
            except:
                country_slab_exact = 'None'

            try:
                date_added = job['date_added']
            except:
                date_added = 'None'

            try:
                date_new = job['date_new']
            except:
                date_new = 'None'

            try:
                date_updated = job['date_updated']
            except:
                date_updated = 'None'

            try:
                description = job['description']
            except:
                description = 'None'

            try:
                django_ct = job['django_ct']
            except:
                django_ct = 'None'

            try:
                django_id = job['django_id']
            except:
                django_id = 'None'

            try:
                federal_contractor = job['federal_contractor']
            except:
                federal_contractor = 'None'

            try:
                guid = job['guid']
            except:
                guid = 'None'

            try:
                id = job['id']
            except:
                id = 'None'

            try:
                is_posted = job['is_posted']
            except:
                is_posted = 'None'

            try:
                lat_long_buid_slab_exact = job['lat_long_buid_slab_exact']
            except:
                lat_long_buid_slab_exact = 'None'

            try:
                location_exact = job['location_exact']
            except:
                location_exact = 'None'

            try:
                network = job['network']
            except:
                network = 'None'

            try:
                on_sites = job['on_sites']
            except:
                on_sites = 'None'

            try:
                onet_exact = job['onet_exact']
            except:
                onet_exact = 'None'

            try:
                other = job['other']
            except:
                other = 'None'

            try:
                reqid = job['reqid']
            except:
                reqid = 'None'

            try:
                salted_date = job['salted_date']
            except:
                salted_date = 'None'

            try:
                score = job['score']
            except:
                score = 'None'

            try:
                state_short = job['state_short']
            except:
                state_short = 'None'

            try:
                state_short_exact = job['state_short_exact']
            except:
                state_short_exact = 'None'

            try:
                title_exact = job['title_exact']
            except:
                title_exact = 'None'

            try:
                title_slab_exact = job['title_slab_exact']
            except:
                title_slab_exact = 'None'

            try:
                title_slug = job['title_slug']
            except:
                title_slug = 'None'

            
            if os.path.exists('NLEJobs.csv'):
                with open('NLEJobs.csv', 'a', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([GeoLocation, _version_, all_locations, buid, city_exact, city_slab_exact, company_buid_slab, company_buid_slab_exact, company_exact, company_member, company_slab_exact, country_ac, country_exact, country_short_exact, country_slab_exact, date_added, date_new, date_updated, description, django_ct, django_id, federal_contractor, guid, id, is_posted, lat_long_buid_slab_exact, location_exact, network, on_sites, onet_exact, other, reqid, salted_date, score, state_short, state_short_exact, title_exact, title_slab_exact, title_slug])
            else:
                with open('NLEJobs.csv', 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['GeoLocation', '_version_', 'all_locations', 'buid', 'city_exact', 'city_slab_exact', 'company_buid_slab', 'company_buid_slab_exact', 'company_exact', 'company_member', 'company_slab_exact', 'country_ac', 'country_exact', 'country_short_exact', 'country_slab_exact', 'date_added', 'date_new', 'date_updated', 'description', 'django_ct', 'django_id', 'federal_contractor', 'guid', 'id', 'is_posted', 'lat_long_buid_slab_exact', 'location_exact', 'network', 'on_sites', 'onet_exact', 'other', 'reqid', 'salted_date', 'score', 'state_short', 'state_short_exact', 'title_exact', 'title_slab_exact', 'title_slug'])
                    writer.writerow([GeoLocation, _version_, all_locations, buid, city_exact, city_slab_exact, company_buid_slab, company_buid_slab_exact, company_exact, company_member, company_slab_exact, country_ac, country_exact, country_short_exact, country_slab_exact, date_added, date_new, date_updated, description, django_ct, django_id, federal_contractor, guid, id, is_posted, lat_long_buid_slab_exact, location_exact, network, on_sites, onet_exact, other, reqid, salted_date, score, state_short, state_short_exact, title_exact, title_slab_exact, title_slug])


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
    {
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
    },
    {
        'authority': 'example1.com',
        'accept': 'application/json',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8,fr;q=0.7,fr-FR;q=0.6,en-GB;q=0.5',
        'origin': 'https://example1-origin.com',
        'referer': 'https://example1-referer.com/',
        'sec-ch-ua': '"Chromium";v="119", "Microsoft Edge";v="119", "Not=AnotherBrand";v="100"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.2088.47',
        'x-origin': 'example1-origin.com',
    },
    {
        'authority': 'example2.com',
        'accept': 'application/json',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8,fr;q=0.7,fr-FR;q=0.6,en-GB;q=0.5',
        'origin': 'https://example2-origin.com',
        'referer': 'https://example2-referer.com/',
        'sec-ch-ua': '"Chromium";v="120", "Microsoft Edge";v="120", "Not=YetAnotherBrand";v="101"',
        'sec-ch-ua-mobile': '?2',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.2088.48',
        'x-origin': 'example2-origin.com',
    },
    # Add more variations here
]

    return choice(headers)

def apiheadersRotator():
    response = requests.get('https://headers.scrapeops.io/v1/browser-headers',params={'api_key': 'fba52e3f-8ad2-4af3-a04c-e2f567f1fe8e','num_headers': '10'})
    headers = response.json()['result']
    return choice(headers)

def get_website_structure(url, headers, params):
    '''This function purpose is to get the sturcture of the page, it returns:
        1. offset: number of job posts in every page
        2. allPositions: count of all positions
        3. allPages: Number of pages '''
    while True:
        try:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code !=200:
                print('Structure reqeust failled')
                headers = staticUserAgentRotator()
                continue
            print("Sturcture request succeed")
            break
        except:
            print('Structure reqeust failled')
            headers = staticUserAgentRotator()
            continue
    data = response.json()    
    allPositions = int(data['pagination']['total'])
    offset = int(data['pagination']['page_size'])
    allPages = int(data['pagination']['total_pages'])
    return (offset, allPositions, allPages)

if __name__== "__main__":
    main()
