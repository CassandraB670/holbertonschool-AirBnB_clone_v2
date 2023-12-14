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


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display a HTML pages"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
