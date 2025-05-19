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