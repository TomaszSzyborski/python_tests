# Failure
# The assertpy library includes a fail() method to explicitly force a test failure. It can be used like this:

from assertpy import assert_that,fail

def test_fail():
    fail('forced failure')
# A very useful test pattern that requires the fail()
# method is to verify the exact contents of an error message. For example:

from assertpy import assert_that,fail

def test_error_msg():
    try:
        some_func('foo')
        fail('should have raised error')
    except RuntimeError as e:
        assert_that(str(e)).is_equal_to('some err')

# In the above code, we invoke some_func()
# with a bad argument which raises an exception.
# The exception is then handled by the try..except block
# and the exact contents of the error message are verified.
# Lastly, if an exception is not thrown by some_func()
# as expected, we fail the test via fail().
#
# This pattern is only used when you need to verify the contents
# of the error message.
# If you only wish to check for an expected exception
# (and don't need to verify the contents of the error message itself),
# you're much better off using a test runner that supports expected exceptions.
# Nose provides a @raises decorator. Pytest has a pytest.raises method.

# Expected Exceptions
# We recommend you use your test runner to check for expected exceptions
# (Pytest's pytest.raises context or Nose's @raises decorator).
# In the special case of invoking a function,
# assertpy provides its own expected exception handling via a simple fluent API.

# Given a function some_func():

def some_func(arg):
    raise RuntimeError('some err')
# We can expect a RuntimeError with:

assert_that(some_func).raises(RuntimeError).when_called_with('foo')
# Additionally, the error message contents are chained, and can be further verified:

assert_that(some_func).raises(RuntimeError).when_called_with('foo')\
    .is_length(8).starts_with('some').is_equal_to('some err')
# Custom Error Messages
# Sometimes you need a little more information in your failures.
#  For this case, assertpy includes a described_as()
# helper that will add a custom message when a failure occurs.
# For example, if we had these failing assertions:

assert_that(1+2).is_equal_to(2)
assert_that(1+2).described_as('adding stuff').is_equal_to(2)
# When run (separately, of course), they would produce these errors:

# Expected <3> to be equal to <2>, but was not.
# [adding stuff] Expected <3> to be equal to <2>, but was not.
# The described_as() helper causes the custom message adding stuff to
# be prepended to the front of the second error.

