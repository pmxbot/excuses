.. image:: https://img.shields.io/pypi/v/excuses.svg
   :target: https://pypi.org/project/excuses

.. image:: https://img.shields.io/pypi/pyversions/excuses.svg

.. image:: https://github.com/pmxbot/excuses/actions/workflows/main.yml/badge.svg
   :target: https://github.com/pmxbot/excuses/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. image:: https://readthedocs.org/projects/excuses/badge/?version=latest
   :target: https://excuses.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2025-informational
   :target: https://blog.jaraco.com/skeleton

BOFH Excuse Generator

Running
=======

``python excuses.py EXCUSES_BASE``

``EXCUSES_BASE`` is the path to a directory that contains ``excuses.html`` and
``excuses.txt``.

The application runs on ``127.0.0.1:8082`` and hosts an index page. Raw new
excuses are available at the ``/new`` path.
