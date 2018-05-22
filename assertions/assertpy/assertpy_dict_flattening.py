from assertpy import  assert_that



fred = {'first_name': 'Fred', 'last_name': 'Smith'}
bob = {'first_name': 'Bob', 'last_name': 'Barr'}
people = [fred, bob]

assert_that(people).extracting('first_name').is_equal_to(['Fred','Bob'])
assert_that(people).extracting('first_name').contains('Fred','Bob')