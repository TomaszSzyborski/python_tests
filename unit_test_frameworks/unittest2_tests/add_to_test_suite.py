import unittest2

class AddToTestSuite(unittest2.TestCase):
    def test_addTest__TestSuite(self):
        class Foo(unittest2.TestCase):
            def test(self): pass

        suite_2 = unittest2.TestSuite([Foo('test')])

        suite = unittest2.TestSuite()
        suite.addTest(suite_2)

        self.assertEqual(suite.countTestCases(), 1)
        self.assertEqual(list(suite), [suite_2])
        # countTestCases() still works after tests are run
        suite.run(unittest2.TestResult())
        self.assertEqual(suite.countTestCases(), 1)

    # "Add all the tests from an iterable of TestCase and TestSuite
    # instances to this test suite."
    #
    # "This is equivalent to iterating over tests, calling addTest() for
    # each element"