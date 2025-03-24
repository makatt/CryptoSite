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
        year=datetime.now().year,  # Текущий год
        coindesk='https://www.coindesk.com',  # Сайт CoinDesk
        coinbase_learn='https://www.coinbase.com/learn',  # Обучение от Coinbase
        coinmarketcap='https://coinmarketcap.com',  # CoinMarketCap
        trezor='https://www.trezor.io',  # Официальный сайт Trezor
        bitcoin_info='/bitcoin',  # Внутренняя ссылка на страницу о Биткойне
        ethereum_org='https://ethereum.org',  # Официальный сайт Ethereum
        litecoin_info='/litecoin',  # Внутренняя ссылка на страницу о Лайткойне
        coindesk_news='https://www.coindesk.com',  # Новости от CoinDesk
        bitcoin_how_it_works='https://www.bitcoin.org/en/how-it-works'  # Как работает Биткойн
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
