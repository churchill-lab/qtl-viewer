import requests


def split_url(url):
    """Splits the given URL into a tuple of (protocol, host, uri)"""
    proto, rest = url.split(':', 1)
    rest = rest[2:].split('/', 1)
    host, uri = (rest[0], rest[1]) if len(rest) == 2 else (rest[0], "")
    return (proto, host, uri)


def parse_url(url):
    """Parses out Referer info indicating the request is from a previously proxied page.
    For example, if:
        Referer: http://localhost:8080/proxy/google.com/search?q=foo
    then the result is:
        ("google.com", "search?q=foo")
    """

    proto, host, uri = split_url(url)

    print ("url={}".format(url))

    print ("{}, {}, {}".format(proto, host, uri))

    if uri.find("/") < 0:
        return None

    first, rest = uri.split("/", 1)

    return {'proto':proto, 'host':host, 'uri':uri, 'url':rest}



@app.route('/proxy/<path:url>', methods=['GET'])
def proxy_get(url):
    rd = parse_url(request.url)
    print("rd=", str(rd))
    #print ('request.path={}'.format(request.path))
    #print ('request.full_path={}'.format(request.full_path))
    #print ('request.script_root={}'.format(request.script_root))
    #print ('request.base_url={}'.format(request.base_url))
    #print ('request.url={}'.format(request.url))
    #print ('request.url_root={}'.format(request.url_root))

    LOG.debug("Fetching {}".format(url))

    #_params = {} if params is None else params
    r = requests.get(rd['url']) #, params=_params)

    print("From cache: {}".format(r.from_cache))
    print('headers=', dict(r.headers))
    return Response(r.content, headers=dict(r.headers)), r.status_code

