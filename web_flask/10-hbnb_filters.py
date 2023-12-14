#!/usr/bin/python3
""" Script that starts a Flask application"""

from flask import Flask, render_template
from models import storage
from sqlalchemy.orm import scoped_session
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception=None):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """display a HTML page"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
