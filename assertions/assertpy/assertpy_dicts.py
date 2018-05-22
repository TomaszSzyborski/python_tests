from assertpy import assert_that

assert_that({}).is_not_none()
assert_that({}).is_empty()
assert_that({}).is_false()
assert_that({}).is_type_of(dict)
assert_that({}).is_instance_of(dict)

assert_that({'a':1,'b':2}).is_length(2)
assert_that({'a':1,'b':2}).is_not_empty()
assert_that({'a':1,'b':2}).is_equal_to({'a':1,'b':2})
assert_that({'a':1,'b':2}).is_equal_to({'b':2,'a':1})
assert_that({'a':1,'b':2}).is_not_equal_to({'a':1,'b':3})

assert_that({'a':1,'b':2}).contains('a')
assert_that({'a':1,'b':2}).contains('b','a')
assert_that({'a':1,'b':2}).does_not_contain('x')
assert_that({'a':1,'b':2}).does_not_contain('x','y')
assert_that({'a':1,'b':2}).contains_only('a','b')
assert_that({'a':1,'b':2}).is_subset_of({'a':1,'b':2,'c':3})

# contains_key() is just an alias for contains()
assert_that({'a':1,'b':2}).contains_key('a')
assert_that({'a':1,'b':2}).contains_key('b','a')

# does_not_contain_key() is just an alias for does_not_contain()
assert_that({'a':1,'b':2}).does_not_contain_key('x')
assert_that({'a':1,'b':2}).does_not_contain_key('x','y')

assert_that({'a':1,'b':2}).contains_value(1)
assert_that({'a':1,'b':2}).contains_value(2,1)
assert_that({'a':1,'b':2}).does_not_contain_value(3)
assert_that({'a':1,'b':2}).does_not_contain_value(3,4)

assert_that({'a':1,'b':2}).contains_entry({'a':1})
assert_that({'a':1,'b':2}).contains_entry({'a':1},{'b':2})
assert_that({'a':1,'b':2}).does_not_contain_entry({'a':2})
assert_that({'a':1,'b':2}).does_not_contain_entry({'a':2},{'b':1})