.. image:: https://img.shields.io/pypi/v/excuses.svg
   :target: https://pypi.org/project/excuses

.. image:: https://img.shields.io/pypi/pyversions/excuses.svg

.. image:: https://img.shields.io/pypi/dm/excuses.svg

.. image:: https://img.shields.io/travis/yougov/excuses/master.svg
   :target: http://travis-ci.org/yougov/excuses

BOFH Excuse Generator

License
=======

License is indicated in the project metadata (typically one or more
of the Trove classifiers). For more details, see `this explanation
<https://github.com/jaraco/skeleton/issues/1>`_.

Running
=======

``python excuses.py EXCUSES_BASE``

``EXCUSES_BASE`` is the path to a directory that contains ``excuses.html`` and
``excuses.txt``.

The application runs on ``127.0.0.1:8082`` and hosts an index page. Raw new
excuses are available at the ``/new`` path.
