import requests

import pytest
from assertpy import assert_that
from assertpy import soft_assertions

def test_request():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )
    (assert_that(response.json(), "response")
        .contains_entry({'id': 1}))


if __name__ == '__main__':
    test_request()
