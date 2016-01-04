# this has all the globals

import os
import web
import sys
import ConfigParser

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


params = {}
params['customization'] = {}
params['customization']['title']      = config.get('customization', 'title')
params['customization']['intro_text'] = config.get('customization', 'intro_text')
params['customization']['theme']      = config.get('customization', 'theme')

params['modules'] = {}
params['modules']['library'] = config.get('modules', 'library')

params['directories'] = {}
params['directories']['media'] = config.get('directories', 'media')


render = web.template.render('templates/', base = 'layout')