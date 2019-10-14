from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources, get_articles






# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting news sources
    news_source = get_sources()
    
    title = 'Home - Welcome to The best News  Highlight Website Online'
    return render_template('index.html', title = title,news_source = news_source )

@main.route('/news/<id>')
def news(id):
    article = get_articles(id)
    print(article)
    return render_template('article.html',article = article)

 