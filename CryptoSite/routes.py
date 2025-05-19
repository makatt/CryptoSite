# -*- coding: utf-8 -*-
import json
import re
from datetime import datetime
import os
from bottle import route, view, request, redirect, static_file, response
from bottle import route, run, view, request, redirect, static_file
from bottle import route, run, template, request, redirect, static_file, view
import sys
import io

REVIEWS_FILE = 'data/reviews.json'

def load_reviews():
    """Загрузка отзывов из файла reviews.json"""
    if not os.path.exists(REVIEWS_FILE):
        return {}
    try:
        with open(REVIEWS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError, UnicodeDecodeError):
        return {}

def save_reviews(reviews_data):
    """Сохранение отзывов в файл reviews.json"""
    try:
        with open(REVIEWS_FILE, 'w', encoding='utf-8') as f:
            json.dump(reviews_data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Ошибка сохранения отзывов: {e}")

def validate_phone(phone):
    """Проверяет формат +7XXXXXXXXXX"""
    return bool(re.match(r'^\+7\d{10}$', phone))

def validate_date(date_str):
    """Проверяет формат ГГГГ-ММ-ДД"""
    return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', date_str))

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

@route('/bitcoin', method=['GET', 'POST'])
@view('bitcoin')
def bitcoin():
    title = 'История Биткойна'
    year = datetime.now().year

    reviews_all = load_reviews()
    btc_reviews = reviews_all.get('bitcoin', [])

    error = None
    if request.method == 'POST':
        name  = request.forms.get('name', '').strip()
        text  = request.forms.get('text', '').strip()
        phone = request.forms.get('phone', '').strip()

        # Валидация
        if not all([name, text, phone]):
            error = 'Пожалуйста, заполните все поля.'
        elif not validate_phone(phone):
            error = 'Телефон должен быть в формате +7XXXXXXXXXX'
        else:
            # Дата теперь проставляем сами
            date = datetime.now().strftime('%Y-%m-%d')
            review = {
                'name':  name,
                'text':  text,
                'date':  date,
                'phone': phone
            }
            btc_reviews.insert(0, review)
            reviews_all['bitcoin'] = btc_reviews
            save_reviews(reviews_all)
            redirect('/bitcoin')

    return {
        'title':     title,
        'year':      year,
        'reviews':   btc_reviews,
        'error':     error,
        'form_data': request.forms
    }



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
    author = text = date = email = ''
    articles = load_articles()

    if request.method == 'POST':
        author = request.forms.get('author', '').strip()
        text = request.forms.get('text', '').strip()
        date = request.forms.get('date', '').strip()
        email = request.forms.get('email', '').strip()

        # Валидация
        if not author or not text or not date or not email:
            error = 'Пожалуйста, заполните все поля.'
        elif re.search(r'\d', author):
            error = 'Имя автора не должно содержать цифр.'
        elif not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
            error = 'Дата должна быть в формате ГГГГ-ММ-ДД.'
        elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            error = 'Введите корректный e-mail.'
        elif len(text) < 100:
            error = 'Текст статьи должен содержать не менее 100 символов.'
        else:
            # Добавление статьи и сортировка по дате (свежие сверху)
            articles.insert(0, {
                'author': author,
                'text': text,
                'date': date,
                'email': email
            })
            save_articles(articles)
            redirect('/articles')  # Сброс POST-запроса и очистка формы

    return {
        'year': datetime.now().year,
        'error': error,
        'author': author,
        'text': text,
        'date': date,
        'email': email,
        'articles': articles
    }


# АКТУАЛЬНЫЕ НОВОСТИ

# Принудительно устанавливаем UTF-8 кодировку
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Создаем папку data, если ее нет
if not os.path.exists('data'):
    os.makedirs('data')

NEWS_FILE = 'data/cryptonews.json'

def load_news():
    """Загрузка новостей о криптовалютах из файла"""
    if not os.path.exists(NEWS_FILE):
        return []
    try:
        with open(NEWS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError, UnicodeDecodeError) as e:
        print(f"Ошибка загрузки файла: {e}")
        return []

def save_news(news_data):
    """Сохранение новостей в файл"""
    try:
        with open(NEWS_FILE, 'w', encoding='utf-8') as f:
            json.dump(news_data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Ошибка сохранения файла: {e}")

@route('/newspage')
@view('newspage')
def show_news():
    """Отображение страницы с новостями о криптовалютах"""
    news_items = load_news()
    # Сортировка по дате (новые сначала)
    news_items.sort(key=lambda x: x.get('date', ''), reverse=True)
    return dict(
        title='Новые криптовалюты',
        year=datetime.now().year,
        news_items=news_items,
        error=None,
        form_data={}
    )

@route('/newspage', method='POST')
def add_crypto():
    """Добавление новой криптовалюты"""
    # Получаем данные из формы
    form_data = {
        'title': request.forms.getunicode('title', '').strip(),
        'symbol': request.forms.getunicode('symbol', '').strip().upper(),
        'date': request.forms.getunicode('date', '').strip(),
        'price': request.forms.getunicode('price', '0').strip(),
        'website': request.forms.getunicode('website', '').strip(),
        'content': request.forms.getunicode('content', '').strip(),
        'status': request.forms.getunicode('status', 'upcoming').strip()
    }
    
    # Валидация данных
    error = None
    if not form_data['title'] or len(form_data['title']) < 2:
        error = "Название монеты должно содержать минимум 2 символа"
    elif not form_data['symbol'] or len(form_data['symbol']) < 2:
        error = "Символ монеты должен содержать минимум 2 символа"
    elif not form_data['date']:
        error = "Укажите дату запуска"
    elif not form_data['content'] or len(form_data['content']) < 10:
        error = "Описание должно содержать минимум 10 символов"
    
    # Загружаем текущие данные
    news_items = load_news()
    
    if error:
        return template('newspage',
            title='Новые криптовалюты',
            year=datetime.now().year,
            news_items=news_items,
            error=error,
            form_data=form_data
        )
    
    try:
        # Преобразуем цену в число
        price = float(form_data['price']) if form_data['price'] else 0.0
    except ValueError:
        price = 0.0
    
    # Создаем новую запись
    new_crypto = {
        'title': form_data['title'],
        'symbol': form_data['symbol'],
        'date': form_data['date'],
        'price': f"{price:.2f}",
        'website': form_data['website'] if form_data['website'].startswith('http') else f"http://{form_data['website']}",
        'content': form_data['content'],
        'status': form_data['status'],
        'id': len(news_items) + 1
    }
    
    # Добавляем и сохраняем
    news_items.append(new_crypto)
    save_news(news_items)
    
    # Перенаправляем с подсветкой новой записи
    redirect(f'/newspage?highlight={new_crypto["id"]}')

@route('/static/<filename:path>')
def serve_static(filename):
    """Отдача статических файлов"""
    return static_file(filename, root='static')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)