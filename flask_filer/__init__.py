from fs.osfs import OSFS
from flask import current_app

from .api import BrowseAPI, DownloadAPI, UploadAPI


class Filer(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['flask-filer'] = self

        self._set_default_config(app)
        self._set_default_fs(app)
        self._set_default_api(app)

    def _set_default_config(self, app):
        app.config.setdefault('FILER_ROOT_PATH', app.root_path)

    def _set_default_fs(self, app):
        self.dfs = OSFS(app.config.get('FILER_ROOT_PATH'))

    def _set_default_api(self, app):
        browse_view = BrowseAPI.as_view('filer-browse')
        app.add_url_rule('/filer-browse/', view_func=browse_view)
        app.add_url_rule('/filer-browse/<path:path>', view_func=browse_view, methods=['GET'])

        download_view = DownloadAPI.as_view('filer-download')
        app.add_url_rule('/filer-download/', view_func=download_view)
        app.add_url_rule('/filer-download/<path:path>', view_func=download_view, methods=['GET'])

        upload_view = UploadAPI.as_view('filer-upload')
        app.add_url_rule('/filer-upload/', view_func=upload_view)
        app.add_url_rule('/filer-upload/<path:path>', view_func=upload_view, methods=['POST'])

    def change_dir(self, cd_path):
        current_app.config['FILER_ROOT_PATH'] = cd_path
        self.dfs = OSFS(current_app.config.get('FILER_ROOT_PATH'))
