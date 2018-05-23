import time
import logging


def timing(test_function):
    logging.basicConfig(level=logging.INFO)
    started_at = time.time()

    test_function()

    elapsed = time.time() - started_at
    logging.info(f"{test_function.__name__()}, {round(elapsed,3)}")
