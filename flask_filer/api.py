import os
import logging

from flask import json, jsonify, request, send_file, current_app
from flask.views import MethodView
from werkzeug.utils import secure_filename

from .utils import get_dirlist, get_details, open_file
from .exceptions import InvalidPathError

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
LOG.addHandler(logging.StreamHandler())


class BrowseAPI(MethodView):

    def get(self, path='/'):
        filer_list = get_dirlist(path)
        LOG.debug(filer_list)
        return json.dumps(get_details(filer_list))


class DownloadAPI(MethodView):

    def get(self, path=None):
        fp = open_file(path)
        LOG.debug(fp)
        return send_file(fp, as_attachment=True, attachment_filename=os.path.basename(path))


class UploadAPI(MethodView):

    def post(self, path=''):
        target = os.path.join(current_app.config['FILER_ROOT_PATH'], path)
        LOG.debug(target)
        if not os.path.isdir(target):
            raise InvalidPathError(path=target)
        else:
            for uploaded_file in request.files.getlist('file'):
                file_path = os.path.join(target, secure_filename(uploaded_file.filename))
                uploaded_file.save(file_path)
            return jsonify(msg='upload successed')
