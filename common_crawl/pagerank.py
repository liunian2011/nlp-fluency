import json
import tldextract
import requests

API_KEY = 'osoo4wswg4g4gc0s0okw8osc0wck4488kg00gs4o'

def get_values(domain_list):
    values = []
    domains_param = "&domains[]=".join(domain_list)
    url = f"https://openpagerank.com/api/v1.0/getPageRank?domains[]={domains_param}"

    headers = {
        'API-OPR': API_KEY
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data and 'response' in data:
            return data['response']
        else:
            return [{"error": "No data found"}]

    except requests.exceptions.RequestException as e:
        return [{"error": str(e)}]

if __name__=='__main__':
    domains = ["google.com", "facebook.com", "twitter.com"]
    results = get_values(domains)
    for result in results:
        print(f"{result['domain']}: PR {result['page_rank_decimal']}")