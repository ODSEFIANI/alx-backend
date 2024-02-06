#!/usr/bin/env python3
""" internationalization"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ clss config """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    # Check if 'locale' parameter is present in the URL
    requested_locale = request.args.get('locale')

    # If the requested locale is valid, return it
    if requested_locale in app.config['LANGUAGES']:
        return requested_locale

    # Otherwise, use the default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """home page """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
