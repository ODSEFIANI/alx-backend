#!/usr/bin/env python3
""" internationalization"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

import pytz

app = Flask(__name__)
babel = Babel(app)

class Config:
    """ class config """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@app.before_request
def before_request():
    user_id = request.args.get('login_as')
    g.user = get_user(user_id)

def get_user(user_id):
    return users.get(int(user_id), None)

@babel.localeselector
def get_locale():
    # 1. Locale from URL parameters
    requested_locale = request.args.get('locale')
    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale

    # 2. Locale from user settings
    if g.user and 'locale' in g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # 3. Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone():
    # 1. Find timezone parameter in URL parameters
    requested_timezone = request.args.get('timezone')
    if requested_timezone:
        try:
            pytz.timezone(requested_timezone)
            return requested_timezone
        except pytz.UnknownTimeZoneError:
            pass

    # 2. Find time zone from user settings
    if g.user and 'timezone' in g.user:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.UnknownTimeZoneError:
            pass

    # 3. Default to UTC
    return 'UTC'

@app.route('/', strict_slashes=False)
def index() -> str:
    """home page """
    return render_template('7-index.html')

if __name__ == '__main__':
    app.run()
