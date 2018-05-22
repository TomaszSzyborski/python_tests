# Soft Assertions
# Normally, an assertion failure will halt test execution immediately by raising an error. Soft assertions are way to collect assertion failures together, to be raise all at once at the end, without halting your test. To use soft assertions in assertpy, just use the with soft_assertions() context manager, like this:

from assertpy import assert_that, soft_assertions

with soft_assertions():
    assert_that('foo').is_length(4)
    assert_that('foo').is_empty()
    assert_that('foo').is_false()
    assert_that('foo').is_digit()
    assert_that('123').is_alpha()
    assert_that('foo').is_upper()
    assert_that('FOO').is_lower()
    assert_that('foo').is_equal_to('bar')
    assert_that('foo').is_not_equal_to('foo')
    assert_that('foo').is_equal_to_ignoring_case('BAR')

# At the end of the block, all assertion failures are collected together and a single AssertionError is raised:

# AssertionError: soft assertion failures:
# 1. Expected <foo> to be of length <4>, but was <3>.
# 2. Expected <foo> to be empty string, but was not.
# 3. Expected <False>, but was not.
# 4. Expected <foo> to contain only digits, but did not.
# 5. Expected <123> to contain only alphabetic chars, but did not.
# 6. Expected <foo> to contain only uppercase chars, but did not.
# 7. Expected <FOO> to contain only lowercase chars, but did not.
# 8. Expected <foo> to be equal to <bar>, but was not.
# 9. Expected <foo> to be not equal to <foo>, but was.
# 10. Expected <foo> to be case-insensitive equal to <BAR>, but was not.
# Also, note that only assertion failures are collected, errors such as TypeError or ValueError are raised immediately. Triggering an explicit test failure with fail() will similarly halt execution immediately. If you need more forgiving behavior, you can use soft_fail() which is collected like any other failing assertion within a soft assertions block.
