#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""sample hello world flask"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, world!<?h1>"