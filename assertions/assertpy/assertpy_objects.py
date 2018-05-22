from assertpy import assert_that


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def say_hello(self):
        return f"Hello, {self.first_name}!"


fred = Person('Fred', 'Smith')

assert_that(fred).is_not_none()
assert_that(fred).is_true()
assert_that(fred).is_type_of(Person)
assert_that(fred).is_instance_of(object)
assert_that(fred).is_same_as(fred)

assert_that(fred.first_name).is_equal_to('Fred')
assert_that(fred.name).is_equal_to('Fred Smith')
assert_that(fred.say_hello()).is_equal_to('Hello, Fred!')

# extracting attributes from objects
fred = Person('Fred', 'Smith')
bob = Person('Bob', 'Barr')
people = [fred, bob]

assert_that(people).extracting('first_name').is_equal_to(['Fred', 'Bob'])
assert_that(people).extracting('first_name').contains('Fred', 'Bob')
assert_that(people).extracting('first_name').does_not_contain('Charlie')


# extracting from subclasses:

class Developer(Person):
    def say_hello(self):
        return f"{self.first_name} writes code."


fred = Person('Fred', 'Smith')
joe = Developer('Joe', 'Coder')
people = [fred, joe]

assert_that(people).extracting('first_name').contains('Fred', 'Joe')

assert_that(people).extracting('first_name', 'last_name').contains(('Fred', 'Smith'), ('Joe', 'Coder'))

assert_that(people).extracting('name').contains('Fred Smith', 'Joe Coder')
assert_that(people).extracting('say_hello').contains('Hello, Fred!', 'Joe writes code.')

# As noted above, the extracting helper also works on a collection of dicts:

fred = {'first_name': 'Fred', 'last_name': 'Smith'}
bob = {'first_name': 'Bob', 'last_name': 'Barr'}
people = [fred, bob]

assert_that(people).extracting('first_name').contains('Fred', 'Bob')

# extracting and filtering

users = [
    {'user': 'Fred', 'age': 36, 'active': True},
    {'user': 'Bob', 'age': 40, 'active': False},
    {'user': 'Johnny', 'age': 13, 'active': True}
]

# The filter can be the name of a key (or attribute, or property, or zero-argument method)
# and the extracted items are kept if the corresponding value is truthy:

assert_that(users).extracting('user', filter='active') \
    .is_equal_to(['Fred', 'Johnny'])

# The filter can be a dict-like object and the extracted items are kept
# if all corresponding key-value pairs are equal:

assert_that(users).extracting('user', filter={'active': False}) \
    .is_equal_to(['Bob'])
assert_that(users).extracting('user', filter={'age': 36, 'active': True}) \
    .is_equal_to(['Fred'])

# The filter can be any function (including an in-line lambda)
# that accepts as its single argument each item in the collection and
# the extracted items are kept if the function evaluates to True:

assert_that(users).extracting('user', filter=lambda x: x['age'] > 20) \
    .is_equal_to(['Fred', 'Bob'])



# The extracting helper can include a sort to enforce order on the extracted items.
#
# The sort can be the name of a key (or attribute, or property, or zero-argument method)
# and the extracted items are ordered by the corresponding values:

assert_that(users).extracting('user', sort='age').is_equal_to(['Johnny','Fred','Bob'])


# The sort can be an iterable of names and the extracted items are ordered
# by corresponding value of the first name,
# ties are broken by the corresponding values of the second name, and so on:

assert_that(users).extracting('user', sort=['active','age']).is_equal_to(['Bob','Johnny','Fred'])
# The sort can be any function (including an in-line lambda)
# that accepts as its single argument each item in the collection
# and the extracted items are ordered by the corresponding function return values:

assert_that(users).extracting('user', sort=lambda x: -x['age'])\
    .is_equal_to(['Bob','Fred','Johnny'])

# Dynamic Assertions on Objects
# When testing attributes of an object,
# the basic assertpy assertions can get a little verbose like this:

fred = Person('Fred','Smith')

assert_that(fred.first_name).is_equal_to('Fred')
assert_that(fred.name).is_equal_to('Fred Smith')
assert_that(fred.say_hello()).is_equal_to('Hello, Fred!')
# So, assertpy takes advantage of the awesome dyanmism
# in the Python runtime to provide dynamic assertions in
# the form of has_<name>() where <name> is the name of any attribute,
# property, or zero-argument method on the given object.

# Using dynamic assertions, we can rewrite the above
# assertions in a more compact and readable way like this:

assert_that(fred).has_first_name('Fred')
assert_that(fred).has_name('Fred Smith')
assert_that(fred).has_say_hello('Hello, Fred!')
# Since fred has the attribute first_name, the dynamic assertion method has_first_name()
# is available. Similarly, the property name can be tested via has_name()
# and the zero-argument method say_hello() via the has_say_hello() assertion.

# As noted above, dynamic assertions also work on dicts:

fred = {'first_name': 'Fred', 'last_name': 'Smith'}

assert_that(fred).has_first_name('Fred')
assert_that(fred).has_last_name('Smith')

