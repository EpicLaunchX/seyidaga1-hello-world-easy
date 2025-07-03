import pytest

from src.pytemplate.utils.welcome import welcome


def test_welcome():
    assert welcome() == "Hello, World!"
