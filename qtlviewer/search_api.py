from __future__ import print_function

import json
import logging
import sys
import time
from datetime import datetime

from flask import Flask, render_template, request, Response, make_response, g
from flask_cors import CORS
import requests
import requests_cache

from flask_basicauth import BasicAuth

app = Flask(__name__)
CORS(app)
app.config['BUNDLE_ERRORS'] = True
basic_auth = BasicAuth(app)

LOG = logging.getLogger('qtl_viewer')

# INSTALL CACHE
requests_cache.install_cache()


class Config:
    pass


class Cache:
    def __init__(self):
        self.urls = {}


CONF = Config()
CACHE = Cache()


def str2bool(val):
    return str(val).lower() in ['true', '1', 't', 'y', 'yes']


@app.before_request
def before_request():
    g.URL_BASE = request.url_root

    if 'HTTP_X_FORWARDED_PATH' in request.environ:
        if 'wsgi.url_scheme' in request.environ:
            protocol = request.environ['wsgi.url_scheme'] + ':'
        g.URL_BASE = "{}//{}{}".format(protocol, request.environ['HTTP_X_FORWARDED_HOST'], request.environ['HTTP_X_FORWARDED_PATH'])

    if g.URL_BASE[-1] == '/':
        g.URL_BASE = g.URL_BASE[:-1]


def format_time(start, end):
    """
    Format length of time between start and end.

    :param start: the start time
    :param end: the end time
    :return: a formatted string of hours, minutes, and seconds
    """
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds)


def configure_logging(verbose):
    handler = logging.StreamHandler(sys.stdout)
    if verbose:
        LOG.setLevel(logging.DEBUG)
    else:
        LOG.setLevel(logging.INFO)

    LOG.addHandler(handler)


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

    if uri.find("/") < 0:
        return None

    first, rest = uri.split("/", 1)

    return {'proto':proto, 'host':host, 'uri':uri, 'url':rest}



@app.route('/proxy/<path:url>', methods=['GET'])
def proxy_get(url):
    #print ('request.url={}'.format(request.url))
    rd = parse_url(request.url)
    '''
    print("rd=", str(rd))
    print ('request.path={}'.format(request.path))
    print ('request.full_path={}'.format(request.full_path))
    print ('request.script_root={}'.format(request.script_root))
    print ('request.base_url={}'.format(request.base_url))
    print ('request.url={}'.format(request.url))
    print ('request.url_root={}'.format(request.url_root))
    print ('request.method={}'.format(request.method))
    print("Fetching {}".format(url))
    '''
    _url = rd['url']


    #_params = {} if params is None else params
    r = requests.get(_url)  # , params=_params)
    #print("\nFrom cache: {}".format(r.from_cache))

    #print(str(CACHE.urls))

    if _url in CACHE.urls:
        CACHE.urls[_url]['hits'] += 1
    else:
        CACHE.urls[_url] = {'hits': 1}

    CACHE.urls[_url]['last'] = datetime.now()

    return Response(r.content, headers=dict(r.headers)), r.status_code


@app.route('/_cache/clear', methods=['GET'])
def cache_clear():
    requests_cache.clear()
    CACHE.urls = {}
    return 'OK'


@app.route('/_cache/view', methods=['GET'])
@basic_auth.required
def cache_view():
    return render_template('_cache.html', CACHE=CACHE, CONF=CONF)


@app.route("/")
def index():
    # POST search_term = request.form.get("search_term")
    # GET  search_term = request.args.get("search_term")
    # BOTH search_term = request.values.get("search_term")
    #print request.path
    #print request.full_path
    #print request.script_root
    #print request.url
    #print request.base_url
    #print request.url_root

    search_term = request.values.get('search_term', '')

    return render_template('index.html', search_term=search_term, CONF=CONF)


@app.route("/new")
def new():
    search_term = request.values.get('search_term', '')

    return render_template('new.html', search_term=search_term, CONF=CONF)


@app.route("/blank")
def blank():
    search_term = request.values.get('search_term', '')

    return render_template('blank.html', search_term=search_term, CONF=CONF)

@app.route("/hc")
def hc():
    search_term = request.values.get('search_term', '')

    return render_template('hc.html', search_term=search_term, CONF=CONF)

def run(host, port, debug):
    print("running...")
    CONF.URL_BASE = app.config['URL_BASE']
    CONF.PLOT_LOD_LINES = app.config.get('PLOT_LOD_LINES', None)
    CONF.PLOT_LOD_XAXIS_TEXT = app.config.get('PLOT_LOD_XAXIS_TEXT', None)
    CONF.PLOT_EFFECT_STRAINS = app.config.get('PLOT_EFFECT_STRAINS', None)
    CONF.API_R_BASE = app.config.get('API_R_BASE', None)

    app.config['BASIC_AUTH_USERNAME'] = 'admin'
    app.config['BASIC_AUTH_PASSWORD'] = 'admin'

    app.run(host=host, port=port, debug=debug, threaded=True)

