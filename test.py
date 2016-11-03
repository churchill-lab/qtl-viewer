from flask import Flask, render_template, request, abort, Response, redirect
import requests
import logging

app = Flask(__name__.split('.')[0])
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger("proxy.py")


@app.route('/proxy', methods=['POST'])
def proxy():
    # POST search_term = request.form.get("search_term")
    # GET  search_term = request.args.get("search_term")
    # BOTH search_term = request.values.get("search_term")

    ## test implementing proxy server for caching of data


    method = request.form.get("method")
    url = request.form.get("url")
    data = request.form.get("data")
    response_type = request.form.get("response_type")

    if method == 'POST':
        r = requests.post(url, data=data)
    elif method == 'GET':
        r = requests.get(url)
    else:
        return 'oops'

    if response_type == 'JSON':
        return r.json
    elif response_type == 'BIN':
        return r.content
    else:
        return r.text

    return 'nothing'




if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)