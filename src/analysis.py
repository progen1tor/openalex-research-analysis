import pandas as pd 
import numpy as np 
from processing import openalex_dataframe


# BASE STATISTICS 
def get_publication_count(df: pd.DataFrame) -> int: 
    return df.id.nunique()

def get_time_range(df: pd.DataFrame) -> tuple[int, int]:
    '''Returns minimum and maximum year of publication'''
    return df.publication_year.min(), df.publication_year.max()

def distribution_by_language(df: pd.DataFrame) -> pd.DataFrame:  # ! note 1 in file 
    data = df.groupby('language').agg(publication_count=('id', 'nunique'))
    return data.sort_values(['publication_count', 'language'], ascending=[False, True])
print(distribution_by_language(openalex_dataframe))

def publication_types(df: pd.DataFrame) -> pd.DataFrame:
    data = df.groupby('type').agg(publication_count=('id', 'nunique'))
    return data.sort_values(['publication_count', 'type'], ascending=[False, True])


# PUBLICATION ANALYSIS 
def number_of_publications_by_year(df: pd.DataFrame) -> pd.DataFrame:
    data = df.groupby('publication_year').agg(publication_count=('id', 'nunique'))
    return data.sort_values('publication_year')

def number_of_publications_by_type(df: pd.DataFrame) -> pd.DataFrame:  # ! note 2 in file 
    '''Comparison of the distribution of different publication types by year and determination of which research formats were most common in different years'''
    data = df.pivot_table(index='publication_year', columns='type', values='id', aggfunc='nunique', fill_value=0)
    return data.sort_index()

def open_access_statistics(df: pd.DataFrame) -> pd.DataFrame:
    data = df.groupby('publication_year').agg(
        cnt=('id', 'nunique'), 
        oacnt=('open_access', 'sum')
        )
    data['open_access_pct'] = (data.oacnt / data.cnt * 100).round(3)
    data['open_access_pct_change'] = (data.open_access_pct.pct_change() * 100).round(3)
    data.open_access_pct_change = data.open_access_pct_change.fillna(0)  # ?
    data.open_access_pct_change = data.open_access_pct_change.mask(data.open_access_pct_change == np.inf, 0)  # ? 
    return data.drop(columns=['cnt', 'oacnt'])