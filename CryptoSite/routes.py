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
        ethereum_page='/ethereum',
        litecoin_org='https://litecoin.org',
        litecoin_info='/litecoin',
        coindesk_news='https://www.coindesk.com',
        bitcoin_how_it_works='https://www.bitcoin.org/en/how-it-works'

    )

@route('/ethereum')
@view('ethereum')
def ethereum():
    """Renders the home page."""
    return dict(
        year=datetime.now().year,
        ethereum_org='https://ethereum.org',  # Официальный сайт Ethereum
        ethereum_what_is='https://ethereum.org/what-is-ethereum',  # Что такое Ethereum
        ethereum_smart_contracts='https://ethereum.org/smart-contracts',  # Смарт-контракты
        ethereum_dapps='https://ethereum.org/dapps',  # Децентрализованные приложения (DApps)
        ethereum_how_it_works='https://ethereum.org/en/staking/#what-is-staking',  # Как работает Ethereum
        ethereum_whitepaper='https://ethereum.org/whitepaper',  # Официальный Whitepaper
        ethereum_github='https://github.com/ethereum',  # Исходный код на GitHub
        ethereum_community='https://ethereum.org/community'  # Сообщество Ethereum
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Контакты',
        year=datetime.now().year
    )

@route('/news')
@view('news')
def news():
    """Renders the news page."""
    return dict(
        title='Новости',
        year=datetime.now().year
    )

@route('/bitcoin')
@view('bitcoin')
def news():
    """Renders the bitcoin page."""
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