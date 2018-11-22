from flask import Flask, request, flash, render_template
from flask_filer import Filer

app = Flask(__name__)
filer = Filer(app)
app.config['SECRET_KEY'] = 'advance.app_filer secret'
app.config['FILER_ROOT_PATH'] = '/var/'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cd_path = request.form.get('filerPath')
        filer.change_dir(cd_path)
        flash('Change Directory to {}'.format(cd_path))
    return render_template('index.html', current_dir=app.config['FILER_ROOT_PATH'])


@app.route('/browsing/')
def browsing():
    # TODO:
    return 'browsing'
