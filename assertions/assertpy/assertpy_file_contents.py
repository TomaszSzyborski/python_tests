from assertpy import assert_that, contents_of

contents = contents_of('foo.txt', 'ascii')
assert_that(contents).starts_with('foo').ends_with('bar').contains('oob')