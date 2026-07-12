import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
from processing import openalex_dataframe
from constants import GRAPHS_PATH
from analysis import number_of_publications_by_year, open_access_statistics, publication_types, most_popular_themes

def number_of_publications_by_year_graph(df: pd.DataFrame) -> None: 
    data = number_of_publications_by_year(df)
    gr = sns.lineplot(data)
    plt.title('Number of publications by year')
    plt.savefig(f'{GRAPHS_PATH}number_of_publications_by_year.png')
    
number_of_publications_by_year_graph(openalex_dataframe)