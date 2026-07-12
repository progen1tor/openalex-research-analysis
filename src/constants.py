from fake_useragent import UserAgent

START_URL = 'https://api.openalex.org'
USER_AGENT = UserAgent().random
LOG_FILENAME = 'openalex-research-analysis/parser_errors.log'
RAW_DATA_FILENAME = 'openalex-research-analysis/data/raw.json'
GRAPHS_PATH = 'openalex-research-analysis/results/'
PAGE_LIMIT = 10