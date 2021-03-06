import unittest2

class DecoratedTest(unittest2.TestCase):
    def test_decorated_skip(self):
        def decorator(func):
            def inner(*a):
                return func(*a)

            return inner

        class Foo(unittest2.TestCase):
            @decorator
            @unittest2.skip('testing')
            def test_1(self):
                pass

        result = unittest2.TestResult()
        test = Foo("test_1")
        suite = unittest2.TestSuite([test])
        suite.run(result)
        self.assertEqual(result.skipped, [(test, "testing")])