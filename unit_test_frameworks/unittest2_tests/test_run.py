import unittest2
from unittest2.test.support import LoggingResult


class TestRun(unittest2.TestCase):
    def test_run(self):
        events = []
        result = LoggingResult(events)

        class LoggingCase(unittest2.TestCase):
            def run(self, result):
                events.append('run %s' % self._testMethodName)

            def test1(self): pass

            def test2(self): pass

        tests = [LoggingCase('test1'), LoggingCase('test2')]

        unittest2.TestSuite(tests).run(result)

        self.assertEqual(events, ['run test1', 'run test2'])
        # self.assertNotEqual(events, ['run test1', 'run test2'])
