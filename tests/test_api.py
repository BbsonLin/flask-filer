import io


def test_browse(client):
    resp = client.get('/browse/')
    assert resp.status_code == 200
    print(resp.data)


def test_download(client):
    resp = client.get('/download/conftest.py')
    assert resp.status_code == 200


def test_upload(client):
    def genbytesio(nbytes, encoding):
        return io.BytesIO(''.join(map(chr, range(nbytes))).encode(encoding))

    files = {
        'testfile.txt': genbytesio(127, 'ascii'),
        'testfile.bin': genbytesio(255, 'utf-8'),
    }
    resp = client.post('/upload/', data=dict(
        file=[(f_v, f_k) for f_k, f_v in files.items()]
    ))
    assert resp.status_code == 200
