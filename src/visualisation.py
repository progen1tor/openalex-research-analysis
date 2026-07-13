import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
from processing import openalex_dataframe
from constants import GRAPHS_PATH
from analysis import number_of_publications_by_year, open_access_statistics, publication_types, most_popular_themes

def number_of_publications_by_year_graph(df: pd.DataFrame) -> None: 
    data = number_of_publications_by_year(df)
    sns.lineplot(data, color='red')  
    plt.title('Number of Publications by Year')
    plt.savefig(f'{GRAPHS_PATH}number_of_publications_by_year_graph.png', bbox_inches='tight')
    
def open_access_statistics_graph(df: pd.DataFrame) -> None: 
    data = open_access_statistics(df)
    plt.figure(figsize=(15, 8))
    sns.lineplot(data, color='red', lw=2)  
    plt.title('Open Access Percentage by Year')
    plt.xticks(data[::4].index.to_list() + [2026])  
    plt.savefig(f'{GRAPHS_PATH}open_access_statistics_graph.png', bbox_inches='tight')  
    
def publication_types_graph(df: pd.DataFrame) -> None: 
    data = publication_types(df).sum().sort_values(ascending=False)
    data_pt_1 = data.iloc[:3]
    data_pt_2 = data.iloc[3:]
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
    gr1 = sns.barplot(data_pt_1, ax=axes[0], palette=['#141173', '#7B1E7A', '#F9564F'])
    gr2 = sns.barplot(data_pt_2, ax=axes[1], palette=['#B33F62', "#FF9E81", '#F3C677', "#FF4F4F", '#F18805'])
    plt.suptitle('Number of Publication by Type', y=.94, fontsize=20)
    gr1.set_xlabel('type', fontsize=13.5)
    gr2.set_xlabel('type', fontsize=13.5)
    gr1.set_xticklabels(data_pt_1.index.to_list(), fontsize=12)
    gr2.set_xticklabels(data_pt_2.index.to_list(), fontsize=12)
    plt.savefig(f'{GRAPHS_PATH}publication_types_graph.png', bbox_inches='tight')
    
def most_popular_themes_graph(df: pd.DataFrame) -> None: 
    data = most_popular_themes(df).iloc[:10].reset_index()  
    sns.barplot(data, y='primary_topic', x='publication_count', hue='primary_topic', palette='viridis')
    plt.suptitle('Top 10 Popular Topics', x=.2, y=.94, fontsize=14)
    plt.savefig(f'{GRAPHS_PATH}most_popular_themes_graph.png')