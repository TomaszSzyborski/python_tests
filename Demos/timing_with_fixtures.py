import logging
import time

import pytest
from pytest import fixture

# @fixture
# def timing(request):
#     """
#     Timing fixture
#     Shows actual test time execution
#     in INFO logs
#
#     Usage:
#     pytest <test_name> --log-cli-level=info
#     :return:
#     """
#     logging.basicConfig(level=logging.INFO)
#     started_at = time.time()
#
#     yield
#     logging.info(f"{request.node.name} took "
#                  f"{round(time.time() - started_at,3)}s to execute.")


@fixture
def timing(request):
    logging.basicConfig(level=logging.INFO)
    request.started_at = time.time()
    request.time_to_execute = None

    def log_time():
        time_to_execute = time.time() - request.started_at
        logging.info(f"{request.node.name} took "
                     f"{time_to_execute:.3f} s to execute.")

    request.addfinalizer(log_time)

