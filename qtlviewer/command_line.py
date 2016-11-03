from __future__ import print_function

import os
import sys


from search_api import app

import search_api

def main():
    settings_file = ''

    if len(sys.argv) > 1:
        settings_file = sys.argv[1]
    else:
        print('Please supply a configurations/settings file.')
        sys.exit()

    settings_file = os.path.abspath(settings_file)

    try:
        print("Configuring application from: {}".format(settings_file))
        app.config.from_pyfile(settings_file)
    except IOError as ioe:
        print(ioe.strerror)
        sys.exit()

    host = app.config.get('HOST', '0.0.0.0')
    port = app.config.get('PORT', 80)
    threaded = app.config.get('THREADED', True)

    search_api.run(host, port, threaded)

if __name__ == '__main__':
    main()