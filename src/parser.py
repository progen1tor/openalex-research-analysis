import requests 
import json 
import logging 
from urllib.parse import urljoin, urlparse
from src.constants import USER_AGENT, START_URL, LOG_FILENAME, PAGE_LIMIT

logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.ERROR,
    format='[%(asctime)s] [%(levelname)s] - %(message)s'
)

def requester(session: requests.Session, url: str) -> dict | None:
    try: 
        rsp = session.get(url, timeout=10)
        rsp.raise_for_status()
        json_data = rsp.json()
        return json_data 
    
    except json.JSONDecodeError as err:
        logging.error(f'{type(err).__name__}: {err} | {url}')
        return None 
        
    except requests.exceptions.Timeout as err:
        logging.error(f'{type(err).__name__}: {err} | {url}')
        return None 
        
    except requests.exceptions.HTTPError as err:
        logging.error(f'{type(err).__name__}: {err} | {url}')
        return None 
        
    except requests.exceptions.ConnectionError as err:
        logging.error(f'{type(err).__name__}: {err} | {url}')
        return None 
        
    except Exception as err:
        logging.error(f'{type(err).__name__}: {err} | {url}')
        return None 


def works_getter() -> dict | None:
    with requests.Session() as s:
        s.headers.update({'User-Agent': USER_AGENT})
        
        json_data = requester(s, f'{START_URL}/institutions?search=hse')
        if json_data:
            results = json_data.get('results')
            target_id = results[0].get('id') if results else None  # get the tgt id of hse 
            
            if target_id:
                iden = urlparse(target_id).path 
                target_url = urljoin(START_URL, iden)
                
                hse_json_data = requester(s, target_url)
                if hse_json_data:
                    all_works_url = hse_json_data.get('works_api_url') 
                    
                    if all_works_url:
                        res = []
                        page_count = 0 
                        while page_count != PAGE_LIMIT:
                            page_count += 1 
                            all_works_json = requester(s, f'{all_works_url}&page={page_count}&per_page=200')
                            res.extend(all_works_json.get('results'))
                        return res 