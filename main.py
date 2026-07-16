from typing import Any 
from src.constants import RAW_DATA_FILENAME, PROCESSED_DATA_FILENAME, ANALYSIS_RESULTS_PATH, dir_names
from src.parser import works_getter
from src.processing import raw_data_loader, dataframe_preparer
import src.analysis as analysis
import src.visualisation as visualisation
import pandas as pd 
import json 
import sys 
import os 


def create_multiple_dirs(names: list[str] = dir_names) -> None:
    for dir_name in names:
        os.makedirs(dir_name, exist_ok=True)
        
def save_json(data: dict[str, Any]) -> None: 
    '''Save raw OpenAlex response into JSON'''
    with open(RAW_DATA_FILENAME, 'w', encoding='utf-8') as out:
        json.dump(data, out)


def analyser(df: pd.DataFrame, path: str) -> None:
    print(f'Total publications: {analysis.get_publication_count(df)}')
    time_range = analysis.get_time_range(df)
    print(f'Period: {time_range[0]}-{time_range[1]}')

    analysis.publication_types(df).to_csv(f'{path}publication_types.csv')
    analysis.number_of_publications_by_year(df).to_csv(f'{path}publications_by_year.csv')
    analysis.number_of_publications_by_type(df).to_csv(f'{path}publications_by_type.csv')
    analysis.open_access_statistics(df).to_csv(f'{path}open_access_statistics.csv')
    analysis.average_authors_by_year_and_publication_type(df).to_csv(f'{path}authors_dynamic.csv')
    analysis.most_cited_publications(df).to_csv(f'{path}most_cited_publications.csv', index=False)
    analysis.most_popular_themes(df).to_csv(f'{path}most_popular_themes.csv')
    analysis.most_popular_keywords(df).to_csv(f'{path}most_popular_keywords.csv')

    for k, v in zip(
        [
            'Average citations',
            'Median citations',
            'Min citations',
            'Max citations'
        ],
        analysis.citation_statistics(df)
    ):
        print(f'{k}: {v}')
        
        
def visualisator(df: pd.DataFrame) -> None:
    visualisation.number_of_publications_by_year_graph(df)
    visualisation.open_access_statistics_graph(df)
    visualisation.publication_types_graph(df)
    visualisation.most_popular_themes_graph(df)


def main():
    
    # making dirs 
    create_multiple_dirs()

    # get the latest info from API 
    data = works_getter()

    # save info into JSON
    if data is None:
        sys.exit(1)
    else: 
        save_json(data)

    # get raw data & transform it into dataframe 
    raw_data = raw_data_loader(RAW_DATA_FILENAME)
    openalex_dataframe = dataframe_preparer(raw_data)
    openalex_dataframe.to_csv(PROCESSED_DATA_FILENAME, index=False)

    # analysis 
    analyser(openalex_dataframe, ANALYSIS_RESULTS_PATH)
        
    # visualisation 
    visualisator(openalex_dataframe)
    
    
if __name__ == '__main__':
    main()