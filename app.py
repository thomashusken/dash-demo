"""
Main executable
"""
from flask import Flask

from gapminder.main import register_dash

app = Flask(__name__)
app = register_dash(app)
server = app.server

if __name__ == "__main__":
    app.run(debug=True, port=8000)
