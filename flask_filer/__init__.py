from fs.osfs import OSFS

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
        browse_view = BrowseAPI.as_view('browse')
        app.add_url_rule('/browse/', view_func=browse_view)
        app.add_url_rule('/browse/<path:path>', view_func=browse_view, methods=['GET'])

        download_view = DownloadAPI.as_view('download')
        app.add_url_rule('/download/', view_func=download_view)
        app.add_url_rule('/download/<path:path>', view_func=download_view, methods=['GET'])

        upload_view = UploadAPI.as_view('upload')
        app.add_url_rule('/upload/', view_func=upload_view)
        app.add_url_rule('/upload/<path:path>', view_func=upload_view, methods=['POST'])
