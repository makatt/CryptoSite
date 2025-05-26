# -*- coding: utf-8 -*-
import json
import re
import os
from datetime import datetime
from bottle import route, run, view, request, redirect, static_file, template, response

DATA_DIR = 'data'
REVIEWS_FILE = os.path.join(DATA_DIR, 'reviews.json')
ARTICLES_FILE = os.path.join(DATA_DIR, 'articles.json')
NEWS_FILE = os.path.join(DATA_DIR, 'cryptonews.json')

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# --------------- УТИЛИТЫ ЗАГРУЗКИ/СОХРАНЕНИЯ -----------------
def load_json(filepath, default):
    try:
        if not os.path.exists(filepath):
            return default
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return default

def save_json(filepath, data):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Ошибка сохранения {filepath}: {e}")

# --------- ВАЛИДАТОРЫ --------------------
def validate_phone(phone):
    return bool(re.match(r'^\+7\d{10}$', phone))

def validate_date(date_str):
    return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', date_str))

def validate_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))

# ----------------- ГЛАВНЫЕ СТРАНИЦЫ -----------------
@route('/')
@route('/home')
@view('index')
def home():
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

@route('/contact')
@view('contact')
def contact():
    return dict(title='Контакты', year=datetime.now().year)

@route('/news')
@view('news')
def news():
    return dict(title='Новости', year=datetime.now().year)


# ---------------- BITCOIN -------------------
@route('/bitcoin', method=['GET', 'POST'])
@view('bitcoin')
def bitcoin():
    reviews_all = load_json(REVIEWS_FILE, {})
    btc_reviews = reviews_all.get('bitcoin', [])
    error = None

    if request.method == 'POST':
        form_data = {
            'name': request.forms.getunicode('name', '').strip(),
            'text': request.forms.getunicode('text', '').strip(),
            'phone': request.forms.getunicode('phone', '').strip()
        }
        error, cleaned_form_data = add_btc_review(form_data, btc_reviews, reviews_all)
        if error is None:
            redirect('/bitcoin')
        else:
            form_data = cleaned_form_data
    else:
        form_data = {}

    return dict(
        title='История Биткойна',
        year=datetime.now().year,
        reviews=btc_reviews,
        error=error,
        form_data=form_data
    )

def add_btc_review(form_data, btc_reviews, reviews_all):
    name = form_data['name']
    text = form_data['text']
    phone = form_data['phone']
    error = None

    if not all([name, text, phone]):
        error = 'Пожалуйста, заполните все поля.'
    elif not validate_phone(phone):
        error = 'Телефон должен быть в формате +7XXXXXXXXXX'
    else:
        date = datetime.now().strftime('%Y-%m-%d')
        btc_reviews.insert(0, {'name': name, 'text': text, 'date': date, 'phone': phone})
        reviews_all['bitcoin'] = btc_reviews
        save_json(REVIEWS_FILE, reviews_all)
        return None, {}

    return error, form_data

# ---------------- ETHEREUM -------------------
@route('/ethereum')
@view('ethereum')
def ethereum():
    return dict(
        year=datetime.now().year,
        decentralization='/decentralization',
        smart_contracts='/smart_contracts',
        ethereum_org='https://ethereum.org',
        ethereum_what_is='https://ethereum.org/what-is-ethereum',
        ethereum_smart_contracts='https://ethereum.org/smart-contracts',
        ethereum_dapps='https://ethereum.org/dapps',
        ethereum_how_it_works='https://ethereum.org/en/staking/#what-is-staking',
        ethereum_whitepaper='https://ethereum.org/whitepaper',
        ethereum_github='https://github.com/ethereum',
        ethereum_community='https://ethereum.org/community',
        ethereum_graphic='https://ru.tradingview.com/chart/?symbol=BINANCE%3AETHUSDt'
    )

@route('/decentralization')
@view('decentralization')
def decentralization():
    return dict(
        year=datetime.now().year,
        decentralization_wiki='https://ru.wikipedia.org/wiki/Децентрализация',
        decentralization_basics='https://www.investopedia.com/terms/d/decentralization.asp',
        blockchain_decentralization='https://www.coindesk.com/learn/what-is-decentralization-why-is-it-important',
        decentralization_benefits='https://www.forbes.com/sites/forbestechcouncil/2021/03/15/the-benefits-of-decentralization-in-blockchain',
        decentralization_examples='https://www.blockchain-council.org/blockchain/examples-of-decentralized-systems-you-must-know',
        decentralization_how_it_works='https://www.ibm.com/topics/decentralization'
    )

@route('/smart_contracts')
@view('smart_contracts')
def smart_contracts():
    return dict(
        year=datetime.now().year,
        smart_contracts_wiki='https://ru.wikipedia.org/wiki/Смарт-контракт',
        smart_contracts_basics='https://www.investopedia.com/terms/s/smart-contracts.asp',
        smart_contracts_how_it_works='https://www.ibm.com/topics/smart-contracts',
        smart_contracts_benefits='https://www.forbes.com/sites/forbestechcouncil/2021/03/15/the-benefits-of-smart-contracts',
        smart_contracts_examples='https://www.blockchain-council.org/blockchain/smart-contract-examples',
        smart_contracts_creation='https://ethereum.org/en/developers/docs/smart-contracts'
    )

# ---------------- LITECOIN -------------------
@route('/litecoin', method=['GET', 'POST'])
@view('litecoin')
def litecoin():
    users_all = load_json('data/users.json', {})
    ltc_users = users_all.get('litecoin', [])
    error = None
    form_data = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'username': '',
        'description': '',
        'phone': ''
    }

    if request.method == 'POST':
        form_data = {
            'username': request.forms.getunicode('username', '').strip(),
            'description': request.forms.getunicode('description', '').strip(),
            'date': request.forms.getunicode('date', '').strip(),
            'phone': request.forms.getunicode('phone', '').strip()
        }
        
        error, cleaned_form_data = add_ltc_user(form_data, ltc_users, users_all)
        form_data = cleaned_form_data

    return dict(
        title='Лайткойн (LTC)',
        year=datetime.now().year,
        users=ltc_users,
        error=error,
        username=form_data.get('username', ''),
        description=form_data.get('description', ''),
        date=form_data.get('date', ''),
        phone=form_data.get('phone', ''),
        binance='https://binance.org/',
        coinbase='https://www.coinbase.com/',
        kraken='https://kraken.com/',
        litecoin_official='https://litecoin.org',
        reddit='https://reddit.com/r/litecoin'
    )

def add_ltc_user(form_data, ltc_users, users_all):
    username = form_data['username']
    description = form_data['description']
    date = form_data['date']
    phone = form_data['phone']
    error = None

    if not username:
        error = 'Пожалуйста, укажите имя пользователя'
    elif not description:
        error = 'Пожалуйста, добавьте описание'
    elif len(description) < 10:
        error = 'Описание должно содержать минимум 10 символов'
    elif not date:
        error = 'Пожалуйста, укажите дату'
    elif not phone:
        error = 'Пожалуйста, укажите телефон'
    elif not validate_phone(phone):
        error = 'Телефон должен быть в формате +7XXXXXXXXXX (11 цифр после +7)'
    else:
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            error = 'Неверный формат даты. Используйте ГГГГ-ММ-ДД'
        
        if not error:
            if any(user['username'].lower() == username.lower() for user in ltc_users):
                error = 'Пользователь с таким именем уже существует'
            else:
                ltc_users.insert(0, {
                    'username': username,
                    'description': description,
                    'date': date,
                    'phone': phone
                })
                
                users_all['litecoin'] = ltc_users
                
                try:
                    save_json('data/users.json', users_all)
                    return None, {}
                except Exception as e:
                    error = f'Ошибка сохранения данных: {str(e)}'

    return error, form_data

# ---------------- Как это работает --------------------
@route('/how-it-works')
@view('howitworks')
def how_it_works():
    return dict(title='Как это работает', year=datetime.now().year)

# ----------------ПОЛЕЗНЫЕ СТАТЬИ ----------------------
@route('/articles', method=['GET', 'POST'])
@view('articles')
def articles():
    articles = load_json(ARTICLES_FILE, [])
    error = ''
    form = {'author': '', 'text': '', 'date': '', 'email': ''}

    if request.method == 'POST':
        form['author'] = request.forms.getunicode('author', '').strip()
        form['text'] = request.forms.getunicode('text', '').strip()
        form['date'] = request.forms.getunicode('date', '').strip()
        form['email'] = request.forms.getunicode('email', '').strip()

        if not all(form.values()):
            error = 'Пожалуйста, заполните все поля.'
        elif re.search(r'\d', form['author']):
            error = 'Имя автора не должно содержать цифр.'
        elif not validate_date(form['date']):
            error = 'Дата должна быть в формате ГГГГ-ММ-ДД.'
        elif not validate_email(form['email']):
            error = 'Введите корректный e-mail.'
        elif len(form['text']) < 100:
            error = 'Текст статьи должен содержать не менее 100 символов.'
        else:
            articles.insert(0, dict(form))
            articles.sort(key=lambda x: x.get('date', ''), reverse=True)
            save_json(ARTICLES_FILE, articles)
            redirect('/articles')

    return {
        'year': datetime.now().year,
        'error': error,
        'author': form['author'],
        'text': form['text'],
        'date': form['date'],
        'email': form['email'],
        'articles': articles
    }

# ---------------- НОВОСТИ О КРИПТОВАЛЮТАХ -------------------
@route('/newspage')
@view('newspage')
def show_news():
    news_items = load_json(NEWS_FILE, [])
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
    form_data = {
        'title': request.forms.getunicode('title', '').strip(),
        'symbol': request.forms.getunicode('symbol', '').strip().upper(),
        'date': request.forms.getunicode('date', '').strip(),
        'price': request.forms.getunicode('price', '0').strip(),
        'website': request.forms.getunicode('website', '').strip(),
        'content': request.forms.getunicode('content', '').strip(),
        'status': request.forms.getunicode('status', 'upcoming').strip()
    }

    error = None
    # Проверка обязательных полей
    if not form_data['title'] or len(form_data['title']) < 2:
        error = "Название монеты должно содержать минимум 2 символа"
    elif not form_data['symbol'] or len(form_data['symbol']) < 2:
        error = "Символ монеты должен содержать минимум 2 символа"
    elif not form_data['date']:
        error = "Укажите дату запуска"
    elif not form_data['content'] or len(form_data['content']) < 10:
        error = "Описание должно содержать минимум 10 символов"
    else:
        # Проверка, что дата не больше сегодня
        try:
            input_date = datetime.strptime(form_data['date'], '%Y-%m-%d').date()
            today = datetime.now().date()
            if input_date > today:
                error = "Дата запуска не должна быть в будущем"
        except ValueError:
            error = "Некорректный формат даты. Используйте ГГГГ-ММ-ДД."

    news_items = load_json(NEWS_FILE, [])

    if error:
        return template('newspage',
                        title='Новые криптовалюты',
                        year=datetime.now().year,
                        news_items=news_items,
                        error=error,
                        form_data=form_data
                        )
    try:
        price = float(form_data['price']) if form_data['price'] else 0.0
    except ValueError:
        price = 0.0

    website = form_data['website']
    if website and not website.startswith('http'):
        website = f"http://{website}"

    new_crypto = {
        'title': form_data['title'],
        'symbol': form_data['symbol'],
        'date': form_data['date'],
        'price': f"{price:.2f}",
        'website': website,
        'content': form_data['content'],
        'status': form_data['status'],
        'id': len(news_items) + 1
    }
    news_items.append(new_crypto)
    save_json(NEWS_FILE, news_items)
    redirect(f'/newspage?highlight={new_crypto["id"]}')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
