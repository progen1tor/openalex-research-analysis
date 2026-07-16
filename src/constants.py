from fake_useragent import UserAgent

START_URL = 'https://api.openalex.org'
USER_AGENT = UserAgent().random
LOG_FILENAME = 'openalex-research-analysis/parser_errors.log'
RAW_DATA_FILENAME = 'openalex-research-analysis/data/raw.json'
PROCESSED_DATA_FILENAME = 'openalex-research-analysis/data/processed.csv'
GRAPHS_PATH = 'openalex-research-analysis/results/graphs/'
ANALYSIS_RESULTS_PATH = 'openalex-research-analysis/results/csv/'
PAGE_LIMIT = 10
dir_names = [
    'openalex-research-analysis/data/', 
    'openalex-research-analysis/results/', 
    'openalex-research-analysis/results/graphs', 
    'openalex-research-analysis/results/csv/'
    ]