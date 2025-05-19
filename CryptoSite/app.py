# -*- coding: utf-8 -*-

import json
from bottle import route, run, view, request, template, redirect, static_file, response, hook
from datetime import datetime
import bottle
import os
import sys

import routes


if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    bottle.debug(True)

def wsgi_app():
    return bottle.default_app()

if __name__ == '__main__':
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    @bottle.route('/static/<filepath:path>')
    def server_static(filepath):
        return bottle.static_file(filepath, root=STATIC_ROOT)
    
    bottle.run(server='wsgiref', host=HOST, port=PORT)
    
year = datetime.now().year
binance = "https://www.binance.com"
coinbase = "https://www.coinbase.com"
kraken = "https://www.kraken.com"
litecoin_official = "https://litecoin.org"
reddit = "https://www.reddit.com/r/litecoin"

USERS_FILE = 'active_users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    try:
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_users(users):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

@route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='./static')

@route('/litecoin')
def litecoin_page():    
    return template('litecoin',
                   users=load_users(),
                   username='',
                   description='',
                   date='',
                   phone='',
                   error=None)

@route('/litecoin', method='POST')
def add_user():
    username = request.forms.get('username')
    description = request.forms.get('description')
    date = request.forms.get('date')
    phone = request.forms.get('phone')

    # Validation
    error = None
    if not all([username, description, date, phone]):
        error = "All fields are required"
    elif not phone.startswith('+7') or len(phone) != 12 or not phone[1:].isdigit():
        error = "Phone must be in format +7XXXXXXXXXX"
    else:
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            error = "Invalid date format. Use YYYY-MM-DD"

    if error:
        return template('litecoin',
                      users=load_users(),
                      username=username,
                      description=description,
                      date=date,
                      phone=phone,
                      error=error)
    
    users = load_users()
    users.append({
        'username': username,
        'description': description,
        'date': date,
        'phone': phone
    })
    save_users(users)
    redirect('/litecoin')
