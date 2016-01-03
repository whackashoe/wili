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
    mdir = os.getcwd() + config.get('directories', 'media')
    try:
        os.path.isdir(mdir)
    except:
        print "media directory %s does not exist" % mdir
        sys.exit(1)
except:
    print "media config dir not found"
    print "add: \"media=/some/dir\" to config.ini"
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
            'media':  path_to_dict(os.getcwd() + config.get('directories', 'media'))
        })

        return render.index(params)

if __name__ == "__main__":
    app.run(port=config.get('network', 'port'))

