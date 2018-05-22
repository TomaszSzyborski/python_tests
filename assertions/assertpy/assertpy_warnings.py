# Just A Warning
# There are times when you only want a warning message instead of an failing test.
# In this case, just replace assert_that with assert_warn.
from assertpy import assert_warn

assert_warn('foo').is_length(4)
assert_warn('foo').is_empty()
assert_warn('foo').is_false()
assert_warn('foo').is_digit()
assert_warn('123').is_alpha()
assert_warn('foo').is_upper()
assert_warn('FOO').is_lower()
assert_warn('foo').is_equal_to('bar')
assert_warn('foo').is_not_equal_to('foo')
assert_warn('foo').is_equal_to_ignoring_case('BAR')
# The above assertions just print the following warning messages, and an AssertionError is never raised:
#
# Expected <foo> to be of length <4>, but was <3>.
# Expected <foo> to be empty string, but was not.
# Expected <False>, but was not.
# Expected <foo> to contain only digits, but did not.
# Expected <123> to contain only alphabetic chars, but did not.
# Expected <foo> to contain only uppercase chars, but did not.
# Expected <FOO> to contain only lowercase chars, but did not.
# Expected <foo> to be equal to <bar>, but was not.
# Expected <foo> to be not equal to <foo>, but was.
# Expected <foo> to be case-insensitive equal to <BAR>, but was not.