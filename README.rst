.. image:: https://img.shields.io/pypi/v/excuses.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/excuses.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/excuses

.. image:: https://github.com/pmxbot/excuses/workflows/Automated%20Tests/badge.svg
   :target: https://github.com/pmxbot/excuses/actions?query=workflow%3A%22Automated+Tests%22
   :alt: Automated Tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. image:: https://readthedocs.org/projects/excuses/badge/?version=latest
   :target: https://excuses.readthedocs.io/en/latest/?badge=latest

BOFH Excuse Generator

Running
=======

``python excuses.py EXCUSES_BASE``

``EXCUSES_BASE`` is the path to a directory that contains ``excuses.html`` and
``excuses.txt``.

The application runs on ``127.0.0.1:8082`` and hosts an index page. Raw new
excuses are available at the ``/new`` path.
