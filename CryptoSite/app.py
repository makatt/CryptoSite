import json
from bottle import route, request, template, redirect
from datetime import datetime
import bottle
import os
import sys

# routes contains the HTTP handlers for our server and must be imported.
import routes


if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    # Debug mode will enable more verbose output in the console window.
    # It must be set at the beginning of the script.
    bottle.debug(True)

def wsgi_app():
    """Returns the application to make available through wfastcgi. This is used
    when the site is published to Microsoft Azure."""
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
        """Handler for static files, used with the development server.
        When running under a production server such as IIS or Apache,
        the server should be configured to serve the static files."""
        return bottle.static_file(filepath, root=STATIC_ROOT)

    # Starts a local test server.
    bottle.run(server='wsgiref', host=HOST, port=PORT)

# for active users
# Configuration variables
year = datetime.now().year
binance = "https://www.binance.com"
coinbase = "https://www.coinbase.com"
kraken = "https://www.kraken.com"
litecoin_official = "https://litecoin.org"
reddit = "https://www.reddit.com/r/litecoin"

# File to store user data
USERS_FILE = 'active_users.json'

def load_users():
    """Loads the list of users from the file."""
    if not os.path.exists(USERS_FILE):
        return []

    try:
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_users(users):
    """Saves the list of users to the file."""
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

@route('/litecoin')
def litecoin():
    return template('litecoin',
                   users=load_users(),
                   username='',
                   description='',
                   date='',
                   phone='',
                   error=None)

@route('/litecoin', method='POST')
def add_litecoin_user():
    username = request.forms.get('username')
    description = request.forms.get('description')
    date = request.forms.get('date')
    phone = request.forms.get('phone')

    # Data validation
    error = None
    if not username or not description or not date or not phone:
        error = "All fields are required."
    elif not phone.startswith('+7') or len(phone) != 12 or not phone[1:].isdigit():
        error = "Phone number must be in the format +7XXXXXXXXXX (e.g., +71234567890)."
    else:
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            error = "Invalid date format. Please use YYYY-MM-DD."

    if error:
        return template('litecoin',
                   users=load_users(),
                   username=username,
                   description=description,
                   date=date,
                   phone=phone,
                   error=error)

    # Add new user
    new_user = {
        'username': username,
        'description': description,
        'date': date,
        'phone': phone
    }

    users = load_users()
    users.append(new_user)
    save_users(users)

    redirect('/litecoin')
