from typing import Any 
from src.constants import RAW_DATA_FILENAME, PROCESSED_DATA_FILENAME, ANALYSIS_RESULTS_PATH
from src.parser import works_getter
from src.processing import raw_data_loader, dataframe_preparer
import src.analysis as analysis
import src.visualisation as visualisation
import json 
import sys 


# get the latest info from API 
data = works_getter()


# save info into JSON 
def save_json(data: dict[str, Any]) -> None: 
    '''Save raw OpenAlex response into JSON'''
    with open(RAW_DATA_FILENAME, 'w', encoding='utf-8') as out:
        json.dump(data, out)
        
if data:
    save_json(data)
else: 
    sys.exit(1)


# get raw data & transform it into dataframe 
raw_data = raw_data_loader(RAW_DATA_FILENAME)
openalex_dataframe = dataframe_preparer(raw_data)
openalex_dataframe.to_csv(PROCESSED_DATA_FILENAME)


# analysis 
print(f'Total publications: {analysis.get_publication_count(openalex_dataframe)}')
time_range = analysis.get_time_range(openalex_dataframe)
print(f'Period: {time_range[0]}-{time_range[1]}')

analysis.publication_types(openalex_dataframe).to_csv(f'{ANALYSIS_RESULTS_PATH}publication_types.csv')
analysis.number_of_publications_by_year(openalex_dataframe).to_csv(f'{ANALYSIS_RESULTS_PATH}publications_by_year.csv')
analysis.number_of_publications_by_type(openalex_dataframe).to_csv(f'{ANALYSIS_RESULTS_PATH}publications_by_type.csv')
analysis.open_access_statistics(openalex_dataframe).to_csv(f'{ANALYSIS_RESULTS_PATH}open_access_statistics.csv')
analysis.average_authors_by_year_and_publication_type(openalex_dataframe).to_csv(f'{ANALYSIS_RESULTS_PATH}authors_dynamic.csv')
analysis.most_cited_publications(openalex_dataframe).to_csv(f'{ANALYSIS_RESULTS_PATH}most_cited_publications.csv')
analysis.most_popular_themes(openalex_dataframe).to_csv(f'{ANALYSIS_RESULTS_PATH}most_popular_themes.csv')
analysis.most_popular_keywords(openalex_dataframe).to_csv(f'{ANALYSIS_RESULTS_PATH}most_popular_keywords.csv')

for k, v in zip(
    [
        'Average citations',
        'Median citations',
        'Min citations',
        'Max citations'
    ],
    analysis.citation_statistics(openalex_dataframe)
):
    print(f'{k}: {v}')
    
    
# visualisation 
visualisation.number_of_publications_by_year_graph(openalex_dataframe)
visualisation.open_access_statistics_graph(openalex_dataframe)
visualisation.publication_types_graph(openalex_dataframe)
visualisation.most_popular_themes_graph(openalex_dataframe)