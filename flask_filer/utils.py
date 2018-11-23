import os
import datetime
import mimetypes
import traceback as tb

from fs.osfs import OSFS
from fs.errors import ResourceNotFound
from flask import current_app


def _get_filer():
    try:
        return current_app.extensions['flask-filer']
    except KeyError:  # pragma: no cover
        raise RuntimeError("You must initialize a Filer with this flask "
                           "application before using this method")


def get_dirlist(dir_path):
    def get_formatted_dirlist(dp):
        dirlist = [os.path.join(dp, filename) for filename in dfs.listdir(dp)]
        return dirlist

    dfs = _get_filer().dfs
    if type(dir_path) == list:
        return [get_formatted_dirlist(dp) for dp in dir_path]
    else:
        return get_formatted_dirlist(dir_path)


def get_info(files=[], namespaces=['details']):
    def get_formatted_info(path_url):
        info = dfs.getinfo(f, namespaces=namespaces).raw
        info['basic']['path_url'] = path_url
        info['basic']['mimetype'] = mimetypes.guess_type(info['basic']['name'])[0]
        info['details']['modified'] = datetime.datetime\
                                              .fromtimestamp(info['details']['modified'])\
                                              .strftime('%Y.%m.%d %H:%M:%S')
        return info

    dfs = _get_filer().dfs
    if type(files) == list:
        files_info = []
        for f in files:
            info = get_formatted_info(f)
            files_info.append(info)
        return files_info
    else:
        return get_formatted_info()


def get_url(files):
    dfs = _get_filer().dfs
    if type(files) == list:
        return [dfs.geturl(f) for f in files]
    else:
        return dfs.geturl(files)


def open_file(file):
    dfs = _get_filer().dfs
    return dfs.open(file)


def change_root_path(cd_path):
    filer = _get_filer()
    current_app.config['FILER_ROOT_PATH'] = cd_path
    filer.dfs = OSFS(current_app.config.get('FILER_ROOT_PATH'))
