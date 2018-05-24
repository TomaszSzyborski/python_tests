# pytest imports
import pytest

# assertpy imports
from assertpy import assert_that
from assertpy import soft_assertions

# requests
import requests

# helpers

# from timing_pytest import timing
# use with @timing decorator

from timing_with_fixtures import timing
# use with timing fixture - as test function parameter


# @timing
def test_request(timing):
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    print(response.json())
    with soft_assertions():
        (assert_that(response.json()["id"], "response id")
         .is_equal_to(1))
        (assert_that(response.json(), "response")
         .contains_entry({'id': 1}))
        (assert_that(response.json(), "response")
         .contains_entry({'id': 2}))
        (assert_that(response.json(), "response")
         .contains_entry({'id': 3}))
        (assert_that(response.json(), "response")
         .contains_entry({'id': 8}))


if __name__ == '__main__':
    test_request()
