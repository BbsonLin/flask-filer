from flask import current_app


def _get_filer():
    try:
        return current_app.extensions['flask-filer']
    except KeyError:  # pragma: no cover
        raise RuntimeError("You must initialize a Filer with this flask "
                           "application before using this method")


def get_dirlist(dirs):
    dfs = _get_filer().dfs
    if type(dirs) == list:
        return [dfs.listdir(d) for d in dirs]
    else:
        return dfs.listdir(dirs)


def get_details(files):
    dfs = _get_filer().dfs
    namespaces = ['details']
    if type(files) == list:
        return [dfs.getinfo(f, namespaces=namespaces).raw for f in files]
    else:
        return dfs.getinfo(files, namespaces=namespaces).raw


def get_url(files):
    dfs = _get_filer().dfs
    if type(files) == list:
        return [dfs.geturl(f) for f in files]
    else:
        return dfs.geturl(files)


def open_file(file):
    dfs = _get_filer().dfs
    return dfs.open(file)
