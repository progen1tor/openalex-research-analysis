import requests 
import json 
from urllib.parse import urljoin, urlparse
from src import USER_AGENT, START_URL

def test():
    with requests.Session() as s:
        s.headers.update({'User-Agent': USER_AGENT})
        rsp = s.get(f'{START_URL}/institutions?search=hse')
        try:
            json_data = rsp.json()
            results = json_data['results']
            target_id = results[0].get('id')  # get the tgt id of hse 
            
            if target_id:
                iden = urlparse(target_id).path
                target_url = urljoin(START_URL, iden)
                hse_rsp = s.get(target_url)
                
                try: 
                    json_hse_data = hse_rsp.json()
                    all_works_url = json_hse_data.get('works_api_url')  # ? is it correct 
                    
                    if all_works_url:
                        rsp_works = s.get(all_works_url)
                        try:
                            all_works_json = rsp_works.json()
                            return all_works_json
                            
                        except json.JSONDecodeError as err:
                            print(err)

                except json.JSONDecodeError as err:
                    print(err)
            
        except json.JSONDecodeError as err:
            print(err)
