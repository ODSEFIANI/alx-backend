#!/usr/bin/env python3
""" internationalization """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Route for the home page.

    Returns:
        str: The rendered HTML content.
    """
    return render_template(
            '0-index.html',
            title='Welcome to Holberton',
            header='Hello world')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
