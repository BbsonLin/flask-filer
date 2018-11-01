
def test_init_app(app):
    assert 'flask-filer' in app.extensions
    assert 'FILER_ROOT_PATH' in app.config
