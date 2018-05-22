from assertpy import assert_that

assert_that(0.0).is_not_none()
assert_that(0.0).is_false()
assert_that(0.0).is_type_of(float)
assert_that(0.0).is_instance_of(float)

assert_that(123.4).is_equal_to(123.4)
assert_that(123.4).is_not_equal_to(456.7)

assert_that(123.4).is_greater_than(100.1)
assert_that(123.4).is_greater_than_or_equal_to(123.4)
assert_that(123.4).is_less_than(200.2)
assert_that(123.4).is_less_than_or_equal_to(123.4)
assert_that(123.4).is_between(100.1, 200.2)
assert_that(123.4).is_close_to(123, 0.5)

assert_that(float('NaN')).is_nan()
assert_that(123.4).is_not_nan()
assert_that(float('Inf')).is_inf()
assert_that(123.4).is_not_inf()