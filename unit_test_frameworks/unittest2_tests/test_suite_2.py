import unittest2


class Test1(unittest2.TestCase):
    def test1(self):
        pass

    def test2(self):
        pass

    def test_count(self):
        test2 = unittest2.FunctionTestCase(lambda: None)
        test3 = unittest2.FunctionTestCase(lambda: None)
        child = unittest2.TestSuite((Test1('test2'), test2))
        parent = unittest2.TestSuite((test3, child, Test1('test1')))

        # print(parent.countTestCases())
        self.assertEqual(parent.countTestCases(), 4)
        # countTestCases() still works after tests are run
        parent.run(unittest2.TestResult())
        self.assertEqual(parent.countTestCases(), 4)
        self.assertEqual(child.countTestCases(), 2)
