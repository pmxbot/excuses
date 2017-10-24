.. image:: https://img.shields.io/pypi/v/excuses.svg
   :target: https://pypi.org/project/excuses

.. image:: https://img.shields.io/pypi/pyversions/excuses.svg

.. image:: https://img.shields.io/travis/yougov/excuses/master.svg
   :target: http://travis-ci.org/yougov/excuses

.. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
   :target: http://skeleton.readthedocs.io/en/latest/?badge=latest

BOFH Excuse Generator

Running
=======

``python excuses.py EXCUSES_BASE``

``EXCUSES_BASE`` is the path to a directory that contains ``excuses.html`` and
``excuses.txt``.

The application runs on ``127.0.0.1:8082`` and hosts an index page. Raw new
excuses are available at the ``/new`` path.
