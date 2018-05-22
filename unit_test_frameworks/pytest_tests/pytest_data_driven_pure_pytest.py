import logging
import sys

import pytest
import math

class ClassToBeTested:
    def __init__(self):
        self.integer = 1
        self.float = 1.0
        self.string = "asdf"


@pytest.mark.parametrize("parameter_value",
                         [math.pi, sys.maxsize, -sys.maxsize,
                          float("inf"), float("-inf"),
                          -1, 1, 2, -123123, 0, -0])
def test_change_integer(parameter_value):
    """
    Change value of initial integer by given value
    :param info_logger - fixture:
    :param parameter_value:
    :return:
    """
    logging.info("Just info")
    logging.warning("Just warning")
    obj = ClassToBeTested()
    initial_value = obj.integer
    assert initial_value == 1
    logging.info("initial value is 1")
    obj.integer += parameter_value
    assert obj.integer == initial_value + parameter_value
    if parameter_value in [-0, 0]:
        with pytest.raises(Exception):
            raise Exception(f"Parameter value should change {obj.__class__.__name__} integer field")


