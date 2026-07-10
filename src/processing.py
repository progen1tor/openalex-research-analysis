import json 
import pandas as pd 
from constants import RAW_DATA_FILENAME
from typing import Any 
from urllib.parse import urlparse 


def raw_data_loader(filename: str = RAW_DATA_FILENAME) -> list[dict[str, Any]]:
    with open(filename, encoding='utf8') as file:
        data = json.load(file)
        return data 
        
        
def id_extractor(url: str) -> str: 
    parts = urlparse(url) 
    return parts.path.lstrip('/')
        

def dataframe_preparer(data: list[dict[str, Any]]) -> pd.DataFrame:
    df = pd.DataFrame(data)
    df = df[
        [
            "id",
            "title",
            'publication_year',
            "publication_date",
            "language",
            "type",
            'cited_by_count',  
            "authorships",  
            "keywords",  
            'primary_topic',  
            'open_access',  
            "awards", 
        ]
    ]
    
    first_author = df.authorships.apply(lambda auth: auth[0]['author']['display_name'] if auth else None)
    df.insert(7, 'first_author', first_author)
    
    author_count = df.authorships.apply(lambda auth: len(auth))
    df.authorships = author_count
    
    kwords = df.keywords.apply(lambda kwds: [kw.get('display_name') for kw in kwds])
    df.keywords = kwords
    
    primary_topics = df.primary_topic.apply(lambda pt: pt.get('display_name'))
    df.primary_topic = primary_topics
    
    access = df.open_access.apply(lambda oa: oa.get('is_oa'))
    df.open_access = access 
    
    awards_cnt = df.awards.apply(lambda a: len(a))
    df.awards = awards_cnt
    df = df.rename(columns={'awards': 'awards_count'})
    
    df.id = df.id.apply(id_extractor)
    
    return df

    
df = dataframe_preparer(raw_data_loader(RAW_DATA_FILENAME))