"""
Main executable
"""
from flask import Flask

from gapminder.main import register_dash

flask = Flask(__name__)
flask = register_dash(flask)

if __name__ == "__main__":
    flask.run(debug=True, port=8000)
