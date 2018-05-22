from assertpy import assert_that

# ignore a single key
assert_that({'a':1,'b':2}).is_equal_to({'a':1}, ignore='b')

# ignore multiple keys using a list
assert_that({'a':1,'b':2,'c':3}).is_equal_to({'a':1}, ignore=['b','c'])

# ignore nested keys using a tuple
assert_that({'a':1,'b':{'c':2,'d':3}}).is_equal_to({'a':1,'b':{'c':2}}, ignore=('b','d'))

# include a single key
assert_that({'a':1,'b':2}).is_equal_to({'a':1}, include='a')

# include multiple keys using a list
assert_that({'a':1,'b':2,'c':3}).is_equal_to({'a':1,'b':2}, include=['a','b'])

# include nested keys using a tuple
assert_that({'a':1,'b':{'c':2,'d':3}}).is_equal_to({'b':{'d':3}}, include=('b','d'))

assert_that({'a':1,'b':{'c':2,'d':3,'e':4,'f':5}}).is_equal_to(
    {'b':{'d':3,'f':5}},
    ignore=[('b','c'),('b','e')],
    include='b'
)

assert_that({'a':1,'b':{'c':2,'d':3,'e':4,'f':5}}).is_equal_to(
    {'b':{'d':3,'f':5}},
    ignore=[('b','c'),('b','e')],
    include='b'
)