import hashlib, base64


def md5(s, as_str=True):
    """ref. https://stackoverflow.com/a/2510935/248616"""
    r = hashlib.md5(s.encode('utf-8')).digest() # r aka. result
    r = base64.b64encode(r)
    if as_str:
        r = r.decode('utf8')
    return r
