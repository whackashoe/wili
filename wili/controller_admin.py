from settings import *
import web

class admin:
    def GET(self):
        return render.admin(params)
    def POST(self):
        try:
            configWrite = open('config.ini', 'r+')
        except:
            return "config.ini not found or could not be read"
        data = web.input()
        config.set('customization', 'title', str(data.set_title))
        config.set('customization', 'intro_text', str(data.set_intro_text))
        config.set('customization', 'intro_subtext', str(data.set_intro_subtext))
        config.set('customization', 'theme', str(data.set_theme))

        # x = web.input(set_image={})
        # if web.debug(x['set_image'].filename):
        #     web.debug(x['set_image'].file.read())
        #     raise web.seeother('/')
        #     return "set an image"

        x = web.input(set_image={})
        filedir = 'static/ui/img' # change this to the directory you want to store the file in.
        if 'set_image' in x: # to check if the file-object is created
            fout = open(filedir +'/header-bg.jpg','w') # creates the file where the uploaded file should be stored
            fout.write(x.set_image.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.

        config.write(configWrite)
        # return "Grrreat success! boe: %s, bax: %s" % (form.d.title)#(form.d.boe, form['bax'].value)

        params['customization']['title']      = config.get('customization', 'title')
        params['customization']['intro_text'] = config.get('customization', 'intro_text')
        params['customization']['intro_subtext'] = config.get('customization', 'intro_subtext')
        params['customization']['theme']      = config.get('customization', 'theme')

        return render.admin(params)