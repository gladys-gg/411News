from app import app
import urllib.request,json
from .models import sources

Sources = sources.Sources

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
      get_sources_url = base_url.format(apiKey)

  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)

    sources_results = None

    if get_sources_response['sources']:
      sources_results_list = get_sources_response['sources']
      sources_results = process_results(sources_results_list)

  return sources_results 

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
       news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        title = news_item.get('title')
        poster = news_item.get('poster_path')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        if poster:
            news_object = News(id,name,title,poster,publishedAt,content)
            news_results.append(news_object)

    return news_results