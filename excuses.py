import os
import random
import sys
import argparse

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

    def pmxbot_excuse(self, client, event, channel, nick, rest):
        args = rest.split(' ')[:2]
        parser = argparse.ArgumentParser()
        parser.add_argument('word', nargs="?")
        parser.add_argument('index', type=int, nargs="?")
        args = parser.parse_args(args)
        if not args.word:
            return self.get()
        return self.find(args.word, args.index)

    @classmethod
    def create_local(cls):
        import pkg_resources
        req = pkg_resources.Requirement.parse('excuses')
        return cls(pkg_resources.resource_filename(req, 'excuses.txt'))

    @classmethod
    def install_pmxbot_command(cls):
        from pmxbot import pmxbot
        generator = cls.create_local()
        pmxbot.command("excuse", aliases=("e ",), doc="Provide a "
            "convenient excuse")(generator.pmxbot_excuse)

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

def setup(base):
    jqpath = os.path.join(base, "jquery-latest.pack.js")
    app_conf = {
        '/static/jquery.js':{
            'tools.staticfile.on':True,
            'tools.staticfile.filename':jqpath,
        },
    }

    cherrypy.tree.mount(ExcusesApp(base), '/', app_conf)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('excuses_base', help="The directory where "
        "excuses.txt and excuses.html can be found.", default=".")
    return parser.parse_args()

def main():
    args = get_args()
    cherrypy.config.update({'server.environment':'production',
                            'server.socket_port':8082,
                            'server.log_to_screen':False,})
    setup(args.excuses_base)
    cherrypy.engine.signal_handler.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()

if __name__ == '__main__':
    main()
