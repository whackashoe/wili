#!/usr/bin/env python2.7

from settings import *

from application import application
from controller_index import index
from controller_admin import admin
from controller_library import library

from web import form


urls = (
    '/',        'index',
    '/admin',   'admin',
    '/library', 'library'
)

app = application(urls, globals())

if __name__ == "__main__":
    app.run(port = config.get('network', 'port'))