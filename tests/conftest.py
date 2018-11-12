import os
import glob
import pytest

from flask import Flask
from flask_filer import Filer


@pytest.fixture
def app():
    app = Flask(__name__)

    filer = Filer()
    filer.init_app(app)

    yield app

    # Clean up the files that unittest generated
    for f in glob.glob('./tests/testfile.*'):
        os.remove(f)


@pytest.fixture
def client(app):
    """A test client for the app."""
    app.config['TESTING'] = True
    return app.test_client()
