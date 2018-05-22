# TODO pytest tests
import pytest


class ClassToBeTested:
    def __init__(self):
        self.integer = 1
        self.float = 1.0
        self.string = "asdf"


#pytest tests

def test_increment_integer():
    """
    Increment integer field of ClassToBeTested object
    :return:
    """
    obj = ClassToBeTested()
    assert obj.integer == 1
    obj.integer += 1
    assert obj.integer == 2

def test_decrement_integer():
    """
    Decrement integer field of ClassToBeTested object
    :return:
    """
    obj = ClassToBeTested()
    assert obj.integer == 1
    obj.integer -= 1
    assert obj.integer == 0
