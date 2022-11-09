"""Providing console commands.

This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         fibonacci = mypackage.skeleton:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This file can be renamed depending on your needs or safely removed if not needed.

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import argparse
import logging
import sys
from typing import List

from mypackage.version import __version__

_logger = logging.getLogger(__name__)


# ---- Python API ----
# The functions defined in this section can be imported by users in their
# Python scripts/interactive interpreter, e.g. via
# `from mypackage.skeleton import fib`,
# when using this Python module as a library.


def fib(n):  # noqa: WPS111
    """Fibonacci example function.

    :param n: integer
    :type n: int

    :returns: n-th Fibonacci number
    """
    assert n > 0  # noqa:S101
    a, b = 1, 1  # noqa:WPS111
    for _ in range(n - 1):
        a, b = b, a + b  # noqa:WPS111
    return a


# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


def parse_args(args: List[str]) -> argparse.Namespace:
    """Parse command line parameters.

    :param args: command line parameters as list of strings
          (for example  ``['--help']``).

    :return: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description='Just a Fibonacci demonstration',
    )
    parser.add_argument(
        '--version',
        action='version',
        version='mypackage {ver}'.format(ver=__version__),
    )
    parser.add_argument(
        dest='n',
        help='n-th Fibonacci number',
        type=int,
        metavar='INT',
    )
    parser.add_argument(
        '-v',
        '--verbose',
        dest='loglevel',
        help='set loglevel to INFO',
        action='store_const',
        const=logging.INFO,
    )
    parser.add_argument(
        '-vv',
        '--very-verbose',
        dest='loglevel',
        help='set loglevel to DEBUG',
        action='store_const',
        const=logging.DEBUG,
    )
    return parser.parse_args(args)


def setup_logging(loglevel: int):
    """Set up the basic logging.

    :param loglevel: minimum loglevel for emitting messages
    """
    logformat = '[%(asctime)s] %(levelname)s:%(name)s:%(message)s'  # noqa:WPS323
    logging.basicConfig(
        level=loglevel,
        stream=sys.stdout,
        format=logformat,
        datefmt='%Y-%m-%d %H:%M:%S',  # noqa:WPS323
    )


def main(args):
    """Provide function calls with string arguments in a CLI fashion.

    :param args: command line parameters as list of strings
          (for example  ``['--verbose', '42']``).
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug('Starting crazy calculations...')
    fib_result = fib(args.n)
    _logger.info(
        'The {0}-th Fibonacci number is {1}'.format(args.n, fib_result),
    )
    _logger.info('Script ends here')


def run():
    """Call `main` passing the CLI arguments extracted from :class::`sys.argv`.

    This function can be used as entry point to create console scripts
    with setuptools.
    """
    main(sys.argv[1:])


if __name__ == '__main__':
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m mypackage.skeleton 42
    run()
