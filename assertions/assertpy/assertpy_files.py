from assertpy import assert_that

assert_that('foo.txt').exists()
assert_that('missing.txt').does_not_exist()
assert_that('foo.txt').is_file()

assert_that('mydir').exists()
assert_that('missing_dir').does_not_exist()
assert_that('mydir').is_directory()

assert_that('foo.txt').is_named('foo.txt')
assert_that('foo.txt').is_child_of('mydir')