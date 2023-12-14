#!/usr/bin/python3
""" Script that starts a Flask application"""

from flask import Flask, render_template
from models import storage
from sqlalchemy.orm import scoped_session
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception=None):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states", defaults={'id': None}, strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id):
    """display a HTML pages"""
    states = storage.all(State)
    if id:
        id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
