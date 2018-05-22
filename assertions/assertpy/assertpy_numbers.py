from assertpy import assert_that

assert_that(0).is_not_none()
assert_that(0).is_false()
assert_that(0).is_type_of(int)
assert_that(0).is_instance_of(int)

assert_that(0).is_zero()
assert_that(1).is_not_zero()
assert_that(1).is_positive()
assert_that(-1).is_negative()

assert_that(123).is_equal_to(123)
assert_that(123).is_not_equal_to(456)

assert_that(123).is_greater_than(100)
assert_that(123).is_greater_than_or_equal_to(123)
assert_that(123).is_less_than(200)
assert_that(123).is_less_than_or_equal_to(200)
assert_that(123).is_between(100, 200)
assert_that(123).is_close_to(100, 25)

assert_that(1).is_in(0,1,2,3)
assert_that(1).is_not_in(-1,-2,-3)