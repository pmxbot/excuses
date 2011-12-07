import os
import random
import sys

import cherrypy


class RandomExcuseGenerator(object):
    def __init__(self, filename):
        file = open(filename)
        self.excuses = [line.strip() for line in file]
        file.close()

    def get(self):
        return random.choice(self.excuses)
    
    def find(self, word, index=None):
        candidates = []
        for e in self.excuses:
            if word in e.lower():
                candidates.append(e)
        imax = len(candidates) - 1
        index = index or random.randint(0, imax)
        if index > imax:
            index = imax
        return candidates[index]
        
class ExcusesApp(object):
    def __init__(self, base):
        self.base_path = base
        self.excuses_path = os.path.join(base, 'excuses.txt')
        self.excuses = RandomExcuseGenerator(self.excuses_path)

    @cherrypy.expose
    def index(self):
        f = open(os.path.join(self.base_path, 'excuses.html'))
        src = f.read()
        f.close()
        return src % self.excuses.get()

    @cherrypy.expose
    def new(self, word=None, index=None):
        if not word:
            return self.excuses.get()
        if index:
            try:
                index = int(index)
            except:
                index = None
        return self.excuses.find(word, index)

def setup():
    base = os.path.abspath(sys.argv[1])
    jqpath = os.path.join(base, "jquery-latest.pack.js")
    app_conf = {
        '/static/jquery.js':{
            'tools.staticfile.on':True,
            'tools.staticfile.filename':jqpath,
        },
    }

    cherrypy.tree.mount(ExcusesApp(base), '/', app_conf)

if __name__ == '__main__':
    cherrypy.config.update({'server.environment':'production', 
                            'server.socket_port':8082,
                            'server.log_to_screen':False,})
    setup()
    cherrypy.engine.signal_handler.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()

