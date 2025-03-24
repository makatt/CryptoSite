"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year,
        coindesk='https://www.coindesk.com',
        coinbase_learn='https://www.coinbase.com/learn',
        coinmarketcap='https://coinmarketcap.com',
        trezor='https://www.trezor.io',
        bitcoin_info='/bitcoin',
        ethereum_org='https://ethereum.org',
        litecoin_info='/litecoin',
        coindesk_news='https://www.coindesk.com',
        bitcoin_how_it_works='https://www.bitcoin.org/en/how-it-works'

    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/news')
@view('news')
def news():
    """Renders the about page."""
    return dict(
        title='Новости',
        year=datetime.now().year
    )

@route('/bitcoin')
@view('bitcoin')
def news():
    """Renders the about page."""
    return dict(
        title='История Биткойна',
        year=datetime.now().year
    )

@route('/litecoin')
@view('litecoin')
def news():
    """Renders the about page."""
    return dict(
        title='История Лайткойна',
        year=datetime.now().year
    )
