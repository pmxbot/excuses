import os
import io
import random
import argparse

import pkg_resources


class RandomExcuseGenerator:
    """
    >>> gen = RandomExcuseGenerator.create_local()
    >>> gen.get()
    '...'
    >>> gen.find('internet').lower()
    '...internet...'
    """
    def __init__(self, filename):
        with io.open(filename, encoding='utf-8') as file:
            self.excuses = [line.strip() for line in file]

    def get(self):
        return random.choice(self.excuses)

    def find(self, word, index=None):
        candidates = [
            e for e in self.excuses
            if word in e.lower()
        ]
        if index is not None:
            candidates = candidates[index:index + 1]
        if not candidates:
            raise ValueError("No matches")
        return random.choice(candidates)

    def pmxbot_excuse(self, rest):
        "Provide a convenient excuse"
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
        from pmxbot import core
        generator = cls.create_local()
        core.command("excuse", aliases="e")(generator.pmxbot_excuse)


class ExcusesApp:
    def __init__(self):
        self.excuses = RandomExcuseGenerator.create_local()

    def index(self):
        stream = pkg_resources.resource_stream('excuses', 'excuses.html')
        with stream:
            src = stream.read().decode('utf-8')
        return src % self.excuses.get()
    index.exposed = True

    def new(self, word=None, index=None):
        if not word:
            return self.excuses.get()
        if index:
            try:
                index = int(index)
            except Exception:
                index = None
        return self.excuses.find(word, index)
    new.exposed = True


def main():
    import cherrypy
    config = {
        'server.environment': 'production',
        'server.socket_port': int(os.environ.get('PORT', 8082)),
        'server.socket_host': '::0',
        'server.log_to_screen': False,
    }
    cherrypy.config.update(config)
    cherrypy.quickstart(ExcusesApp())
