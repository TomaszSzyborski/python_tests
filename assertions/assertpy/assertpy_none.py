from assertpy import assert_that

assert_that(None).is_none()
assert_that('').is_not_none()
assert_that(None).is_type_of(type(None))