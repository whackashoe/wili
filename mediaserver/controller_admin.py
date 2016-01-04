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
        config.set('customization', 'title', str(data.title))
        config.set('customization', 'intro_text', str(data.intro_text))
        config.set('customization', 'theme', str(data.theme))
        config.write(configWrite)
        # return "Grrreat success! boe: %s, bax: %s" % (form.d.title)#(form.d.boe, form['bax'].value)

        params['customization']['title']      = config.get('customization', 'title')
        params['customization']['intro_text'] = config.get('customization', 'intro_text')
        params['customization']['theme']      = config.get('customization', 'theme')

        return render.admin(params)