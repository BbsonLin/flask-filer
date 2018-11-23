from flask import Flask, request, flash, render_template
from flask_filer import Filer
from flask_filer.utils import get_dirlist, get_info, change_root_path

app = Flask(__name__)
app.config['SECRET_KEY'] = 'advance.app_filer secret'
app.config['FILER_ROOT_PATH'] = '/var/'

filer = Filer(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cd_path = request.form.get('filerPath')
        change_root_path(cd_path)
        flash('Change Directory to {}'.format(cd_path))
    return render_template('index.html', current_dir=app.config['FILER_ROOT_PATH'])


@app.route('/browse/')
@app.route('/browse/<path:path>')
def browse(path=''):
    filer_list = get_dirlist(path)
    return render_template('browse.html', file_list=get_info(filer_list))
