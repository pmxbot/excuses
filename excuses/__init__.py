import os
import random
import argparse
import functools
import pathlib

from typing import Union, Any, cast, Iterable

from importlib_resources import files
from importlib_resources.abc import Traversable


@functools.singledispatch
def _resolve_iterable(input: Union[str, pathlib.Path, Traversable, Any]):
    return (line.strip() for line in cast(Iterable[str], input))


# on Python 3.11 or later, replace explicit registration with
# @_resolve_iterable.register
@_resolve_iterable.register(Traversable)
@_resolve_iterable.register(pathlib.Path)
def _(input: Union[pathlib.Path, Traversable]):
    with input.open(encoding='utf-8') as stream:
        yield from _resolve_iterable(stream)


@_resolve_iterable.register
def _(input: str):
    return _resolve_iterable(pathlib.Path(input))


class RandomExcuseGenerator:
    """
    >>> gen = RandomExcuseGenerator.create_local()
    >>> gen.get()
    '...'
    >>> gen.find('internet').lower()
    '...internet...'
    """

    def __init__(self, excuses):
        self.excuses = list(_resolve_iterable(excuses))

    def get(self):
        return random.choice(self.excuses)

    def find(self, word, index=None):
        candidates = [e for e in self.excuses if word in e.lower()]
        if index is not None:
            candidates = candidates[index : index + 1]
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
        return cls(files().joinpath('excuses.txt'))

    @classmethod
    def install_pmxbot_command(cls):
        from pmxbot import core

        generator = cls.create_local()
        core.command("excuse", aliases="e")(generator.pmxbot_excuse)


class ExcusesApp:
    def __init__(self):
        self.excuses = RandomExcuseGenerator.create_local()

    def index(self):
        src = files().joinpath('excuses.html').read_text(encoding='utf-8')
        return src % self.excuses.get()

    index.exposed = True  # type: ignore[attr-defined]

    def new(self, word=None, index=None):
        if not word:
            return self.excuses.get()
        if index:
            try:
                index = int(index)
            except Exception:
                index = None
        return self.excuses.find(word, index)

    new.exposed = True  # type: ignore[attr-defined]


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
