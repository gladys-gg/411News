from flask import render_template
from ..request import get_sources
from . import main


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

        # Getting popular news
    sources = get_sources()

    return render_template('index.html', sources = sources)

# Views
# @main.route('/articles/<sources_id>')
# def articles(source_id):
#     '''
#     View root page function that returns the index page and its data
#     '''

#         # Getting popular articles
#     articles = get_articles()

#     return render_template('articles.html', articles = articles)
    