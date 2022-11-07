import pytest

from mypackage.skeleton import fib, main


def test_fib():
    """API Tests."""
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13  # noqa: WPS432
    with pytest.raises(AssertionError):
        fib(-10)


def test_main(capsys):
    """CLI Tests."""  # noqa: DAR101
    # capsys is a pytest fixture that allows asserts against stdout/stderr
    # https://docs.pytest.org/en/stable/capture.html
    main(['7'])
    captured = capsys.readouterr()
    assert 'The 7-th Fibonacci number is 13' in captured.out
