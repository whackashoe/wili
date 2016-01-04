#!/usr/bin/env python2.7

from application import application
from settings import *
from util import *

from controller_index import index
from controller_admin import admin
from controller_library import library


urls = (
    '/',        'index',
    '/admin',   'admin',
    '/library', 'library'
)

app = application(urls, globals())

if __name__ == "__main__":
    app.run(port = config.get('network', 'port'))

