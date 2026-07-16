# OpenAlex Research Analysis 


## Возможности 
- получение данных из OpenAlex API 
- обработка данных 
- анализ публикаций 
- построение графиков 
- сохранение результатов 

## Структура проекта 
```text
openalex-research-analysis/  
├── data/  
│   ├── raw.json                    
│   └── processed.csv              
│  
├── results/  
│   ├── csv/  
│   │   ├── authors_dynamic.csv  
│   │   ├── most_cited_publications.csv  
│   │   ├── most_popular_keywords.csv  
│   │   ├── most_popular_themes.csv  
│   │   ├── open_access_statistics.csv  
│   │   ├── publication_types.csv  
│   │   ├── publications_by_type.csv  
│   │   └── publications_by_year.csv  
│   │  
│   └── graphs/  
│       ├── most_popular_themes_graph.png  
│       ├── number_of_publications_by_year_graph.png  
│       ├── open_access_statistics_graph.png  
│       └── publication_types_graph.png  
│  
├── src/  
│   ├── __init__.py
│   ├── analysis.py                 
│   ├── constants.py                
│   ├── parser.py                   
│   ├── processing.py              
│   └── visualisation.py            
│  
├── main.py                         
├── requirements.txt                
├── README.md                     
└── .gitignore                      
```