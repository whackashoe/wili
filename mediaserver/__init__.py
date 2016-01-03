#!/usr/bin/env python2.7

import web
import ConfigParser
import os
import glob
import sys
import json


config = ConfigParser.ConfigParser()
try:
    f = open('config.ini')
    config.readfp(open('config.ini'))
except:
    print "config.ini not found or could not be read"
    sys.exit(1)

try:
    port = config.get('network', 'port')
    try:
        int(port)
    except:
        print "port not an integer"
        sys.exit(1)
except:
    print "port config not found"
    print "add: \"port=8080\" to config.ini"
    sys.exit(1)


try:
    mdir = config.get('directories', 'movies')
    try:
        os.path.isdir(mdir)
    except:
        print "movies directory %s does not exist" % mdir
        sys.exit(1)
except:
    print "movies config dir not found"
    print "add: \"movies=/some/dir\" to config.ini"
    sys.exit(1)

try:
    mdir = config.get('directories', 'tv')
    try:
        os.path.isdir(mdir)
    except:
        print "tv directory %s does not exist" % mdir
        sys.exit(1)
except:
    print "tv config dir not found"
    print "add: \"tv=/some/dir\" to config.ini"
    sys.exit(1)

try:
    mdir = config.get('directories', 'music')
    try:
        os.path.isdir(mdir)
    except:
        print "music directory %s does not exist" % mdir
        sys.exit(1)
except:
    print "music config dir not found"
    print "add: \"music=/some/dir\" to config.ini"
    sys.exit(1)


class application(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', int(port)))

def path_to_dict(path):
    # http://stackoverflow.com/questions/25226208/represent-directory-tree-as-json
    d = {'name': os.path.basename(path)}

    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path, x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"

    return d

urls = (
    '/(.*)', 'index'
)

app = application(urls, globals())
render = web.template.render('templates/', base='layout')

class index:
    def GET(self, name):
        params = {}
        params['files'] = json.dumps({
            'movies': path_to_dict(config.get('directories', 'movies')),
            'tv':     path_to_dict(config.get('directories', 'tv')),
            'music':  path_to_dict(config.get('directories', 'music'))
        })

        return render.index(params)

if __name__ == "__main__":
    app.run(port=config.get('network', 'port'))

