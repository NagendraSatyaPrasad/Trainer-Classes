import mathoper
import pytest


def test_add():
    assert mathoper.add(10, 20) == 30


def test_square():
    assert mathoper.square(5) == 25


def test_greet():
    assert mathoper.greet() == "Happy Morning"


def test_quot():
    assert mathoper.quot(10, 2) == 5


def test_quot_zero():
    with pytest.raises(ZeroDivisionError):
        mathoper.quot(10, 0)