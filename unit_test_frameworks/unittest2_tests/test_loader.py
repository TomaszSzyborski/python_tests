import unittest2


class TestLoader(unittest2.TestCase):
    def test_load_tests_from_test_case_no_matches(self):
        class Foo(unittest2.TestCase):
            def foo_bar(self): pass

        empty_suite = unittest2.TestSuite()

        loader = unittest2.TestLoader()
        self.assertEqual(loader.loadTestsFromTestCase(Foo), empty_suite)


    # "Return a suite of all tests cases contained in the TestCase-derived
    # class testCaseClass"
    #
    # What happens if loadTestsFromTestCase() is given an object
    # that isn't a subclass of TestCase? Specifically, what happens
    # if testCaseClass is a subclass of TestSuite?
    #
    # This is checked for specifically in the code, so we better add a
    # test for it.
