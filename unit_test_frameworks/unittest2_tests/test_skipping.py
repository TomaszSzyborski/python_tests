import unittest2

class TestSkipping(unittest2.TestCase):
    def test_skip_doesnt_run_setup(self):
        class Foo(unittest2.TestCase):
            wasSetUp = False
            wasTornDown = False

            def setUp(self):
                Foo.wasSetUp = True

            def tornDown(self):
                Foo.wasTornDown = True

            @unittest2.skip('testing')
            def test_1(self):
                pass

        result = unittest2.TestResult()
        test = Foo("test_1")
        suite = unittest2.TestSuite([test])
        suite.run(result)
        self.assertEqual(result.skipped, [(test, "testing")])
        self.assertFalse(Foo.wasSetUp)
        self.assertFalse(Foo.wasTornDown)