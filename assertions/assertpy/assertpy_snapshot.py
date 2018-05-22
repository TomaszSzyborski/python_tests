# Snapshot Testing
# Take a snapshot of a python data structure,
# store it on disk in JSON format,
# and automatically compare the latest data to the stored data on every test run.
# The snapshot testing features of assertpy are borrowed from Jest,
# a well-kwown and powerful Javascript testing framework.

# For example, snapshot the following dict:
import random

from assertpy import assert_that

assert_that({'a':1,'b':2,'c':3}).snapshot()
# Stored on disk as the following JSON:

# {
#   "a": 1,
#   "b": 2,
#   "c": 3
# }
# Additionally, the on-disk snapshot format supports
# most python data structures (dict, list, object, etc).
# For example:

assert_that(None).snapshot()
assert_that(True).snapshot()
assert_that(123).snapshot()
assert_that(-987.654).snapshot()
assert_that('foo').snapshot()
assert_that([1,2,3]).snapshot()
assert_that(set(['a','b','c'])).snapshot()
assert_that({'a':1,'b':2,'c':3}).snapshot()
assert_that(1 + 2j).snapshot()
# assert_that(someobj).snapshot()
# Snapshot artifacts (typically found in the __snapshots folder),
# should be committed to source control alongside any code changes.

# On the first run (when the snapshot file doesn't yet exist),
#  the snapshot is created,
# stored to disk, and the test is passed.
# On all subsequent runs,
# the given data is compared to the on-disk snapshot,
# and the test fails if they don't match.
# Failure means that some change occured,
# so either a bug or a known implementation changed.

# Updating Snapshots
# It's easy to update your snapshots...
# just delete them all and re-run the test suite to regenerate all snapshots.

# Snapshot Parameters
# By default, snapshots are identified by test filename plus line number.
# Alternately, you can specify a custom identifier using the id keyword:

assert_that({'a':1,'b':2,'c':3}).snapshot(id='my-custom-id')
# By default, all snapshots (including those with custom identifiers)
# are stored in the __snapshots folder.
# Alternately, you can specify a custom path using the path keyword:

assert_that({'a':1,'b':2,'c':3}).snapshot(path='my-custom-folder')

# Snapshot Blackbox
# Functional testing (which snapshot testing falls under)
# is very much blackbox testing.
# When something goes wrong,
# it's hard to pinpoint the issue, because they provide little isolation.
# On the plus side, snapshots can provide enormous leverage as
# a few well-place snapshots can strongly verify application state
# that would require dozens if not hundreds of unit tests.

# Chaining
# One of the nicest aspects of any fluent API is the ability
# to chain methods together. In the case of assertpy,
# chaining allows you to write assertions as single statement
# -- that reads like a sentence, and is easy to understand.

# Here are just a few examples:

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.shoe_size = random.randint(30,50)
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def say_hello(self):
        return f"Hello, {self.first_name}!"


fred = Person('Fred', 'Smith')
bob = Person('Bob', 'Barr')
people = [fred, bob]

assert_that('foo').is_length(3).starts_with('f').ends_with('oo')
assert_that([1,2,3]).is_type_of(list).contains(1,2).does_not_contain(4,5)
assert_that(fred).has_first_name('Fred').has_last_name('Smith').has_shoe_size(12)
assert_that(people).is_length(2).extracting('first_name').contains('Fred','Joe')