.. These are examples of badges you might want to add to your README:
please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/mypackage.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/mypackage
    .. image:: https://readthedocs.org/projects/mypackage/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://mypackage.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/mypackage/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/mypackage
    .. image:: https://img.shields.io/pypi/v/mypackage.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/mypackage/
    .. image:: https://img.shields.io/conda/vn/conda-forge/mypackage.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/mypackage
    .. image:: https://pepy.tech/badge/mypackage/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/mypackage
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/mypackage

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

==========
mypackage
==========


    A fake package to learn github and python package.


A longer description of your project goes here...


.. _pyscaffold-notes:

Making Changes & Contributing
=============================

This project uses `pre-commit`_, please make sure to install it before making any
changes::

    pip install pre-commit
    cd mypackage
    pre-commit install

It is a good idea to update the hooks to the latest version::

    pre-commit autoupdate

Don't forget to tell your contributors to also install and use pre-commit.

.. _pre-commit: https://pre-commit.com/

Note
====

This project has been set up using PyScaffold 4.2.2. For details and usage
information on PyScaffold see https://pyscaffold.org/.
