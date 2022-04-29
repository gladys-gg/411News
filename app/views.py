from flask import render_template
from app import app
from .request import get_sources

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

        # Getting popular news
    popular_news = get_sources('popular')
    print(popular_news)
    title = 'Home - Welcome to The best news Review Website Online'
    return render_template('index.html', title = title,popular = popular_news)
    