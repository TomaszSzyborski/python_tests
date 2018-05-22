from assertpy import assert_that

fred = {'first_name': 'Fred', 'last_name': 'Smith', 'shoe_size': 12}

assert_that(fred).has_first_name('Fred')
assert_that(fred).has_last_name('Smith')
assert_that(fred).has_shoe_size(12)