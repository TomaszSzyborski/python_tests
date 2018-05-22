from assertpy import assert_that
assert_that(()).is_not_none()
assert_that(()).is_empty()
assert_that(()).is_false()
assert_that(()).is_type_of(tuple)
assert_that(()).is_instance_of(tuple)
assert_that(()).is_iterable()

assert_that((1,2,3)).is_length(3)
assert_that((1,2,3)).is_not_empty()
assert_that((1,2,3)).is_equal_to((1,2,3))
assert_that((1,2,3)).is_not_equal_to((1,2,4))

assert_that((1,2,3)).contains(1)
assert_that((1,2,3)).contains(3,2,1)
assert_that((1,2,3)).does_not_contain(4,5,6)
assert_that((1,2,3)).contains_only(1,2,3)
assert_that((1,1,1)).contains_only(1)
assert_that((1,2,3)).contains_sequence(2,3)
assert_that((1,2,3)).is_subset_of((1,2,3,4))

assert_that((1,2,2)).contains_duplicates()
assert_that((1,2,3)).does_not_contain_duplicates()

assert_that((1,2,3)).starts_with(1)
assert_that((1,2,3)).ends_with(3)