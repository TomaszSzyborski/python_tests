#TODO pyshould assertions
from pyshould import *
from pyshould import should
from pyshould import should, should_not, all_of
import unittest2 as unittest

class TestPyShould(unittest.TestCase):
    def test_basic(self):
        result = 5
        result | should.be_integer()
        (1+1) | should_not.equal(1)
        "foo" | should.equal('foo')
        len([1, 2, 3]) | should.be_greater_than(2);

        result += 0.5

        result | should.equal(1/2 + 5)
        1 | should_not.eq(2)
        # Matchers not requiring a param can skip the call parens
        True | should.be_truthy

        # Check for exceptions with the context manager interface
        with should.throw(TypeError):
            raise TypeError('foo')

        with should.not_raise:  # will report a failure
            fp = open('does-not-exists.txt')

        # Apply our custom logic for a test
        'FooBarBaz' | should.pass_callback(lambda x: x[3:6] == 'Bar')

    def test_should_dot(self):
        should.be_an_integer.or_string.and_equal(1)
        # (integer) OR (string AND equal 1)

        should.be_an_integer.or_a_float.or_a_string
        # (integer) OR (float) OR (string)
        should.be_an_integer.or_a_string.and_equal_to(10).or_a_float
        # (integer) OR (string AND equal 10) OR (float)

        should.be_an_integer.or_a_string.but_less_than(10)
        # (integer OR string) AND (less than 10)

        # Note: we can use spacing to make them easier to read
        should.be_an_integer.or_a_string.and_equal(0).or_a_float
        # (integer) OR (string AND equal 0) OR (float)

        # Note: in this case we use capitalization to make them more obvious
        should.be_an_integer.Or_a_string.And_equal(1).But_Not_be_a_float
        # ( (integer) OR (string AND equal 1) ) AND (not float)

        # Note: if no matchers are given the last one is used
        should.be_equal_to(10).Or(20).Or(30)
        # (equal 10) OR (equal 20) OR (equal 30)

        # Note: If no combinator is given AND is used by default
        should.integer.greater_than(10).less_than(20)
        # (integer) AND (greater than 10) AND (less than 20)

        # Note: But by using should_either we can set OR as default
        should_either.equal(10).equal(20).equal(30)
        # (equal 10) OR (equal 20) OR (equal 30)


    def test_other(self):
        it(1).should_equal(1)
        it(0).to_equal(0)
        any_of(1, 3).to_equal(1)
        all_of([1, 3]).should_be_int()
        none_of(1, 3).to_eq(0)
        from pyshould.expect import expect, expect_all, expect_any, expect_none

        expect(1).to_equal(1)
        # Note that matchers without params need the call parens when using this syntax
        expect_all(1, 3).to_be_int()
        expect_any([1, 3]).to_equal(1)
        expect(any_of(1, 3)).to_equal(1)