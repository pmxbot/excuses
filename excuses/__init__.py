import os
import random
import argparse

import pkg_resources

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
        return cls(pkg_resources.resource_filename('excuses', 'excuses.txt'))

    @classmethod
    def install_pmxbot_command(cls):
        from pmxbot import pmxbot
        generator = cls.create_local()
        pmxbot.command("excuse", aliases=("e ",), doc="Provide a "
            "convenient excuse")(generator.pmxbot_excuse)

class ExcusesApp(object):
    def __init__(self, base):
        self.base = base
        if base:
            excuses_filename = os.path.join(self.base, 'excuses.txt')
            self.excuses = RandomExcuseGenerator(excuses_filename)
        else:
            self.excuses = RandomExcuseGenerator.create_local()

    def index(self):
        stream = pkg_resources.resource_stream('excuses', 'excuses.html')
        if self.base:
            stream = open(os.path.join(self.base, 'excuses.html'))
        with stream:
            src = stream.read()
        return src % self.excuses.get()
    index.exposed = True

    def new(self, word=None, index=None):
        if not word:
            return self.excuses.get()
        if index:
            try:
                index = int(index)
            except:
                index = None
        return self.excuses.find(word, index)
    new.exposed = True

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('excuses_base', help="The directory where "
        "excuses.txt and excuses.html can be found.", nargs='?', default=None)
    return parser.parse_args()

def main():
    global cherrypy
    import cherrypy
    args = get_args()
    cherrypy.config.update({'server.environment': 'production',
                            'server.socket_port': 8082,
                            'server.log_to_screen': False, })
    cherrypy.quickstart(ExcusesApp(args.excuses_base))

if __name__ == '__main__':
    main()
