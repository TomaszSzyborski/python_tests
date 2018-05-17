import unittest2


class TestSuite(unittest2.TestCase):
    def test_init_test_suite_instances_in_tests(self):
        def tests():
            ftc = unittest2.FunctionTestCase(lambda: None)
            yield unittest2.TestSuite([ftc])
            yield unittest2.FunctionTestCase(lambda: None)

        suite = unittest2.TestSuite(tests())
        self.assertEqual(suite.countTestCases(), 2)
        # countTestCases() still works after tests are run
        suite.run(unittest2.TestResult())
        self.assertEqual(suite.countTestCases(), 2)
