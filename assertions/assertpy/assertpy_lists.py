from assertpy import assert_that

assert_that([]).is_not_none()
assert_that([]).is_empty()
assert_that([]).is_false()
assert_that([]).is_type_of(list)
assert_that([]).is_instance_of(list)
assert_that([]).is_iterable()

assert_that(['a','b']).is_length(2)
assert_that(['a','b']).is_not_empty()
assert_that(['a','b']).is_equal_to(['a','b'])
assert_that(['a','b']).is_not_equal_to(['b','a'])

assert_that(['a','b']).contains('a')
assert_that(['a','b']).contains('b','a')
assert_that(['a','b']).does_not_contain('x','y')
assert_that(['a','b']).contains_only('a','b')
assert_that(['a','a']).contains_only('a')
assert_that(['a','b','c']).contains_sequence('b','c')
assert_that(['a','b']).is_subset_of(['a','b','c'])

assert_that(['a','x','x']).contains_duplicates()
assert_that(['a','b','c']).does_not_contain_duplicates()

assert_that(['a','b','c']).starts_with('a')
assert_that(['a','b','c']).ends_with('c')