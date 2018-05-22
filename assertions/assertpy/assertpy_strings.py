from assertpy import *

assert_that('').is_not_none()
assert_that('').is_empty()
assert_that('').is_false()
assert_that('').is_type_of(str)
assert_that('').is_instance_of(str)

assert_that('foo').is_length(3)
assert_that('foo').is_not_empty()
assert_that('foo').is_true()
assert_that('foo').is_alpha()
assert_that('123').is_digit()
assert_that('foo').is_lower()
assert_that('FOO').is_upper()
assert_that('foo').is_iterable()
assert_that('foo').is_equal_to('foo')
assert_that('foo').is_not_equal_to('bar')
assert_that('foo').is_equal_to_ignoring_case('FOO')

assert_that(u'foo').is_unicode() # on python 2
assert_that('foo').is_unicode()  # on python 3

assert_that('foo').contains('f')
assert_that('foo').contains('f','oo')
assert_that('foo').contains_ignoring_case('F','oO')
assert_that('foo').does_not_contain('x')
assert_that('foo').contains_only('f','o')
assert_that('foo').contains_sequence('o','o')

assert_that('foo').contains_duplicates()
assert_that('fox').does_not_contain_duplicates()

assert_that('foo').is_in('foo','bar','baz')
assert_that('foo').is_not_in('boo','bar','baz')
assert_that('foo').is_subset_of('abcdefghijklmnopqrstuvwxyz')

assert_that('foo').starts_with('f')
assert_that('foo').ends_with('oo')

assert_that('foo').matches(r'\w')
assert_that('123-456-7890').matches(r'\d{3}-\d{3}-\d{4}')
assert_that('foo').does_not_match(r'\d+')