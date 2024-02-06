from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

# Configure Babel
babel = Babel(app)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@app.route('/<string:name>')
def greet(name: str) -> str:
    """
    Route that greets the user by name.

    Args:
        name (str): The name parameter from the URL.

    Returns:
        str: The rendered HTML content.
    """
    return render_template('1-index.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
