import json 
import pandas as pd 
from constants import RAW_DATA_FILENAME
from typing import Any 


def raw_data_loader(filename: str = RAW_DATA_FILENAME) -> dict[str, Any]:
    with open(filename, encoding='utf8') as file:
        data = json.load(file)
        res = data.get('results')
        if res:
            return res 


def dataframe_formatter(data_dict: dict[str, Any]) -> pd.DataFrame:
    df = pd.DataFrame(data_dict)
    df = df[
        [
            "id",
            "title",
            'publication_year',
            "publication_date",
            "language",
            "type",
            'cited_by_count',  # number of citations
            "authorships",  # * take the 1st author and create another col with author count 
            "keywords",  # get kwords (display name probably) 
            'primary_topic',
            'open_access',  # whether the publication is in the public domain
            "awards",  # turn into count via len 
        ]
    ]
    
    first_author = df.authorships.apply(lambda auth: auth[0]['author']['display_name'])
    df.insert(7, 'first_author', first_author)
    
    author_count = df.authorships.apply(lambda auth: len(auth))
    df.authorships = author_count
    
    kwords = df.keywords.apply(lambda kwds: [kw['display_name'] for kw in kwds])
    df.keywords = kwords
    
    return df

    
print(dataframe_formatter(raw_data_loader(RAW_DATA_FILENAME)))