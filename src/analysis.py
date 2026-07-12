import pandas as pd 


# BASE STATISTICS 
def get_publication_count(df: pd.DataFrame) -> int: 
    return df.id.nunique()

def get_time_range(df: pd.DataFrame) -> tuple[int, int]:
    '''Returns minimum and maximum year of publication'''
    return df.publication_year.min(), df.publication_year.max()

def publication_types(df: pd.DataFrame) -> pd.DataFrame:
    data = df.groupby('type').agg(publication_count=('id', 'nunique'))
    return data.sort_values(['publication_count', 'type'], ascending=[False, True])


# PUBLICATION ANALYSIS 
def number_of_publications_by_year(df: pd.DataFrame) -> pd.DataFrame:
    data = df.groupby('publication_year').agg(publication_count=('id', 'nunique'))
    return data.sort_values('publication_year')

def number_of_publications_by_type(df: pd.DataFrame) -> pd.DataFrame:  
    '''Comparison of the distribution of different publication types by year and determination of which research formats were most common in different years'''
    data = df.pivot_table(index='publication_year', columns='type', values='id', aggfunc='nunique', fill_value=0) 
    return data.sort_index()

def open_access_statistics(df: pd.DataFrame) -> pd.DataFrame:
    data = df.groupby('publication_year').agg(
        publication_count=('id', 'nunique'), 
        open_access_count=('open_access', 'sum')
        )
    data['open_access_pct'] = (data.open_access_count / data.publication_count * 100).round(3)

    return data.drop(columns=['publication_count', 'open_access_count'])

def average_authors_by_year_and_publication_type(df: pd.DataFrame) -> pd.DataFrame:  
    '''How the average number of authors changed over the years, broken down by publication type'''
    pt = df.pivot_table(index='publication_year', columns='type', values='authorships', aggfunc='mean', fill_value=0).round(1)
    return pt 
    

# IMPACT ANALYSIS 
def most_cited_publications(df: pd.DataFrame) -> pd.DataFrame:
    return df[['id', 'title', 'first_author', 'cited_by_count']].sort_values(['cited_by_count', 'title'], ascending=[False, True]).head(20)

def most_popular_themes(df: pd.DataFrame) -> pd.DataFrame:
    data = df.groupby('primary_topic', as_index=False).agg(publication_count=('id', 'nunique'))
    return data[['primary_topic', 'publication_count']].sort_values(['publication_count', 'primary_topic'], ascending=[False, True]).set_index('primary_topic').head(20)

def most_popular_keywords(df: pd.DataFrame) -> pd.DataFrame:
    data = df[['id', 'keywords']].explode('keywords')
    data = data.groupby('keywords', as_index=False).agg(publication_count=('id', 'nunique'))
    return data.sort_values(['publication_count', 'keywords'], ascending=[False, True]).rename(columns={'keywords': 'keyword'}).set_index('keyword').head(20)

def citation_statistics(df: pd.DataFrame) -> pd.DataFrame:
    avg = df.cited_by_count.mean().round()
    med = df.cited_by_count.median().round()
    mn = df.cited_by_count.min()
    mx = df.cited_by_count.max()
    data = pd.Series([avg, med, mn, mx], index=['mean', 'median', 'min', 'max'], dtype='int64')
    return data 