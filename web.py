#!/usr/bin/env python
from bottle import Bottle, run

from web_util import setup_web_app

app = Bottle()
setup_web_app(app)

if __name__ == '__main__':
    run(app, host='localhost', port=8888)
