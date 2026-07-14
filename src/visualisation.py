import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
from constants import GRAPHS_PATH
from analysis import number_of_publications_by_year, open_access_statistics, publication_types, most_popular_themes

def number_of_publications_by_year_graph(df: pd.DataFrame) -> None: 
    data = number_of_publications_by_year(df).reset_index()
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data, 
        x='publication_year', 
        y='publication_count', 
        color='steelblue'
        ) 
    
    plt.title('Number of Publications by Year')
    plt.xlabel('Publication year')
    plt.grid(alpha=.3)
    
    plt.savefig(
        f'{GRAPHS_PATH}number_of_publications_by_year_graph.png', bbox_inches='tight',
        dpi=300
        )
    plt.close()
    
    
def open_access_statistics_graph(df: pd.DataFrame) -> None: 
    data = open_access_statistics(df).reset_index()
    
    plt.figure(figsize=(15, 8))
    sns.lineplot(
        data, 
        x='publication_year', 
        y='open_access_pct', 
        color='#3366CC', 
        lw=2
        )  
    
    plt.title('Open Access Percentage by Year')
    plt.xlabel('Publication year')
    plt.ylabel('Open Access (%)')
    plt.grid(alpha=.3)
    
    plt.savefig(
        f'{GRAPHS_PATH}open_access_statistics_graph.png', 
        bbox_inches='tight',
        dpi=300
        )
    plt.close()  
    
    
def publication_types_graph(df: pd.DataFrame) -> None: 
    data = publication_types(df)
    data_pt_1 = data.loc[data.publication_count >= 50].reset_index()
    data_pt_2 = data.loc[data.publication_count < 50].reset_index()
    
    _, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
    sns.barplot(
        data_pt_1, 
        x='type', 
        y='publication_count', 
        ax=axes[0], palette=['#264653','#2A9D8F','#E9C46A'],
        hue='type'
        )
    sns.barplot(
        data_pt_2, 
        x='type', 
        y='publication_count', 
        ax=axes[1], 
        palette=['#F4A261','#E76F51','#457B9D','#1D3557','#A8DADC'],
        hue='type'
        )
    
    plt.suptitle('Number of Publications by Type', y=.94, fontsize=20)
    axes[0].set_xlabel('Type', fontsize=13.5)
    axes[1].set_xlabel('Type', fontsize=13.5)
    axes[0].tick_params(axis='x', labelsize=12)  
    axes[1].tick_params(axis='x', labelsize=12)
    
    plt.savefig(
        f'{GRAPHS_PATH}publication_types_graph.png', 
        bbox_inches='tight',
        dpi=300
        )
    plt.close()
    
    
def most_popular_themes_graph(df: pd.DataFrame) -> None: 
    data = most_popular_themes(df).iloc[:10].reset_index() 
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data,
        y='primary_topic',
        x='publication_count',
        hue='primary_topic',  
        palette='viridis',
    ) 
    
    plt.suptitle('Top 10 Popular Topics', x=.32, y=.94, fontsize=14)
    plt.xlabel('Number of Publications')
    plt.ylabel('')
    plt.savefig(
        f'{GRAPHS_PATH}most_popular_themes_graph.png', 
        bbox_inches='tight',
        dpi=300
        )
    plt.close()