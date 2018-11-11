from flask import Flask
from flask_filer import Filer

app = Flask(__name__)
filer = Filer(app)


@app.route('/')
def hello():
    return 'hello'
