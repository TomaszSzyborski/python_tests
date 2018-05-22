from assertpy import assert_that

# partial matches, these all pass
assert_that('foo').matches(r'\w')
assert_that('foo').matches(r'oo')
assert_that('foo').matches(r'\w{2}')

# match the entire string with an anchored regex pattern, passes
assert_that('foo').matches(r'^\w{3}$')

# fails
assert_that('foo').matches(r'^\w{2}$')