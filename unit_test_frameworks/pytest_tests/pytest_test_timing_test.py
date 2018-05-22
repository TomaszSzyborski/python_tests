import random

import pytest
# import logging
import time
import pytest
import logging

# timing decorator
def timing(test: callable):
    logging.basicConfig(level=logging.INFO)
    started_at = time.time()
    test()
    elapsed = time.time() - started_at
    logging.info(f"{test.__name__}, {round(elapsed,3)}")


@timing
def test_timing_sleep():
    time.sleep(1)
    assert 1 == 1


@timing
def test_timing_addition():
    sum(range(random.randint(1, 10000)))
    assert 1 == 1