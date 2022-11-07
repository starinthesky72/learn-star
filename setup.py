"""Setup file for mypackage. Use setup.cfg to configure your project.

This file was generated with PyScaffold. PyScaffold helps you to put up
the scaffold of your new Python project. Learn more under:
https://pyscaffold.org/
"""
import warnings

from setuptools import setup

if __name__ == '__main__':
    try:
        setup(use_scm_version={'version_scheme': 'no-guess-dev'})
    except Exception:
        warnings.warn(
            '\n\nAn error occurred while building the project, '
            + 'please ensure you have the most updated version of setuptools, '
            + 'setuptools_scm and wheel with:\n'
            + '   pip install -U setuptools setuptools_scm wheel\n\n',
        )
        raise
