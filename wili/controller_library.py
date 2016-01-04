from settings import *
import json
import os

def path_to_dict(path):
    # http://stackoverflow.com/questions/25226208/represent-directory-tree-as-json
    d = {'name': os.path.basename(path)}

    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path, x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"

    return d

class library:
    def GET(self):
        params['page_specific'] = {}
        params['page_specific']['files'] = json.dumps({
            'media':  path_to_dict(os.getcwd() + config.get('directories', 'media'))
        })

        return render.library(params)