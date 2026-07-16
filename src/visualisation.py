import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
from src.constants import GRAPHS_PATH
from src.analysis import number_of_publications_by_year, open_access_statistics, publication_types, most_popular_themes

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
    plt.ylabel('Open access (%)')
    plt.grid(alpha=.3)
    
    plt.savefig(
        f'{GRAPHS_PATH}open_access_statistics_graph.png', 
        bbox_inches='tight',
        dpi=300
        )
    plt.close()  
    
    
def publication_types_graph(df: pd.DataFrame) -> None: 
    data = publication_types(df).reset_index()
    
    plt.figure(figsize=(10, 5))
    gr = sns.barplot(
        data, 
        x='type', 
        y='publication_count',
        hue='type',
        palette='mako'
    )
    
    for c in gr.containers:
        gr.bar_label(c, fontsize=10, padding=3)
    ymx = data.publication_count.max()
    gr.set_ylim(0, ymx * 1.1)
    
    plt.title('Number of Publications by Type')
    plt.xlabel('Type')
    plt.ylabel('Publication count')
    plt.tick_params(axis='x', labelsize=10, labelrotation=45)
    
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
    plt.xlabel('Number of publications')
    plt.ylabel('')
    plt.savefig(
        f'{GRAPHS_PATH}most_popular_themes_graph.png', 
        bbox_inches='tight',
        dpi=300
        )
    plt.close()