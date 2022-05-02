import urllib.request,json
from .models import Sources,Articles

# Sources = sources.Sources

# Getting api key
api_key = None

# Getting the news base url
base_url = None

def configure_request(app):
  global api_key,sources_base_url,articles_base_url
  api_key = app.config['NEWS_API_KEY']
  sources_base_url = app.config['NEWS_API_SOURCES_URL']
  articles_base_url = app.config['NEWS_API_ARTICLES_URL']


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = 'https://newsapi.org/v2/sources?apiKey=0b09126777674730a031e9037e30d50e'

    with urllib.request.urlopen(get_sources_url) as url:
      get_sources_data = url.read()
      get_sources_response = json.loads(get_sources_data)

      sources_results = None

    if get_sources_response['sources']:
      sources_results_list = get_sources_response['sources']
      sources_results = process_sources(sources_results_list)

    return sources_results 



def process_sources(sources_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain movie details

    Returns :
        sources_results: A list of movie objects
    '''
    sources_results = []
    for sources_item in sources_list:

      id = sources_item.get('id')
      name = sources_item.get('name')
      description = sources_item.get('description')
      url = sources_item.get('url')
      category = sources_item.get('category')
      
        

      if id:
        sources_object = Sources(id,name,category,description,url)
        sources_results.append(sources_object)

    return sources_results


def get_articles(sources_id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = 'https://newsapi.org/v2/everything?q={}&apiKey=0b09126777674730a031e9037e30d50e'.format(sources_id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
      get_articles_data = url.read()
      get_articles_response = json.loads(get_articles_data)

      articles_results = None

    if get_articles_response['articles']:
      articles_results_list = get_articles_response['articles']
      articles_results = process_articles(articles_results_list)

    return articles_results 



def process_articles(articles_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain movie details

    Returns :
        articles_results: A list of movie objects
    '''
    articles_results = []
    for articles_item in articles_list:

      title = articles_item.get('title')
      content = articles_item.get('content')
      url = articles_item.get('url')
      author = articles_item.get('author')
      urlToImage = articles_item.get('urlToImage')
      publishedAt = articles_item.get('publishedAt')
        

      if title:
        articles_object = Articles(title,content,url,author,urlToImage,publishedAt)
        articles_results.append(articles_object)

    return articles_results

