from bottle import route, view, request, redirect
import json
import re
from datetime import datetime
import os

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
        bitcoin_how_it_works='/how-it-works'
    )

@route('/ethereum')
@view('ethereum')
def ethereum():
    """Renders the home page."""
    return dict(
        year=datetime.now().year,
        decentralization='/decentralization',
        smart_contracts='/smart_contracts',
        ethereum_org='https://ethereum.org',  # Официальный сайт Ethereum
        ethereum_what_is='https://ethereum.org/what-is-ethereum',  # Что такое Ethereum
        ethereum_smart_contracts='https://ethereum.org/smart-contracts',  # Смарт-контракты
        ethereum_dapps='https://ethereum.org/dapps',  # Децентрализованные приложения (DApps)
        ethereum_how_it_works='https://ethereum.org/en/staking/#what-is-staking',  # Как работает Ethereum
        ethereum_whitepaper='https://ethereum.org/whitepaper',  # Официальный Whitepaper
        ethereum_github='https://github.com/ethereum',  # Исходный код на GitHub
        ethereum_community='https://ethereum.org/community', # Сообщество Ethereum
        ethereum_graphic = 'https://ru.tradingview.com/chart/?symbol=BINANCE%3AETHUSDt'
    )

@route('/decentralization')
@view('decentralization')
def decentralization():
    """Renders the decentralization page."""
    return dict(
        year=datetime.now().year,  
        decentralization_wiki='https://ru.wikipedia.org/wiki/Децентрализация',  # Ссылка на Википедию
        decentralization_basics='https://www.investopedia.com/terms/d/decentralization.asp',  # Основы децентрализации
        blockchain_decentralization='https://www.coindesk.com/learn/what-is-decentralization-why-is-it-important',  # Децентрализация в блокчейне
        decentralization_benefits='https://www.forbes.com/sites/forbestechcouncil/2021/03/15/the-benefits-of-decentralization-in-blockchain',  # Преимущества децентрализации
        decentralization_examples='https://www.blockchain-council.org/blockchain/examples-of-decentralized-systems-you-must-know',  # Примеры децентрализованных систем
        decentralization_how_it_works='https://www.ibm.com/topics/decentralization'  # Как работает децентрализация
    )

@route('/smart_contracts')
@view('smart_contracts')
def smart_contracts():
    """Renders the smart contracts page."""
    return dict(
        year=datetime.now().year,
        smart_contracts_wiki='https://ru.wikipedia.org/wiki/Смарт-контракт',  # Ссылка на Википедию
        smart_contracts_basics='https://www.investopedia.com/terms/s/smart-contracts.asp',  # Основы смарт-контрактов
        smart_contracts_how_it_works='https://www.ibm.com/topics/smart-contracts',  # Как работают смарт-контракты
        smart_contracts_benefits='https://www.forbes.com/sites/forbestechcouncil/2021/03/15/the-benefits-of-smart-contracts',  # Преимущества смарт-контрактов
        smart_contracts_examples='https://www.blockchain-council.org/blockchain/smart-contract-examples',  # Примеры использования
        smart_contracts_creation='https://ethereum.org/en/developers/docs/smart-contracts'  # Создание смарт-контрактов
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
def bitcoin():
    """Renders the bitcoin page."""
    return dict(
        title='История Биткойна',
        year=datetime.now().year,
        decentralization='/decentralization',
    )

@route('/litecoin')
@view('litecoin')
def litecoin():
    """Renders the about page."""
    return dict(
        title='История Лайткойна',
        year=datetime.now().year,
                binance='https://binance.org/',
        coinbase='https://www.coinbase.com/',
        kraken='https://kraken.com/',
        litecoin_official='https://litecoin.org',
        reddit='https://reddi.com/litecoin'
    )

@route('/how-it-works')
@view('howitworks')
def how_it_works():
    """Renders the about page."""
    return dict(
        title='История Лайткойна',
        year=datetime.now().year
    )

#ПОЛЕЗНЫЕ СТАТЬИ

ARTICLES_FILE = 'data/articles.json'  # путь к файлу с данными 

def load_articles():
    try:
        with open(ARTICLES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_articles(articles):
    with open(ARTICLES_FILE, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)

@route('/articles', method=['GET', 'POST'])
@view('articles')
def articles():
    error = ''
    author = text = date = phone = ''
    articles = load_articles()

    if request.method == 'POST':
        author = request.forms.get('author', '').strip()
        text = request.forms.get('text', '').strip()
        date = request.forms.get('date', '').strip()
        phone = request.forms.get('phone', '').strip()

        # Валидация
        if not author or not text or not date or not phone:
            error = 'Пожалуйста, заполните все поля.'
        elif not re.match(r'^\+7\d{10}$', phone):
            error = 'Телефон должен быть в формате +7XXXXXXXXXX'
        elif not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
            error = 'Дата должна быть в формате ГГГГ-ММ-ДД'
        else:
            # Добавление статьи и сортировка по дате (свежие сверху)
            articles.insert(0, {
                'author': author,
                'text': text,
                'date': date,
                'phone': phone
            })
            save_articles(articles)
            redirect('/articles')  # Чтобы сбросить POST и очистить форму

    return {
        'year': datetime.now().year,
        'error': error,
        'author': author,
        'text': text,
        'date': date,
        'phone': phone,
        'articles': articles
    }