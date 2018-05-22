from assertpy import assert_that
assert_that(True).is_true()
assert_that(False).is_false()
assert_that(True).is_type_of(bool)