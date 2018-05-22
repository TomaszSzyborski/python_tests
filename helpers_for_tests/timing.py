import time
import unittest
import logging


class SlowTestCase(unittest.TestCase):
    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        print('{} ({}s)'.format(self.id(), round(elapsed, 2)))

    def test_should_run_fast(self):
        self.assertEqual(1, 1)

    def test_should_run_slow(self):
        time.sleep(0.5)
        self.assertEqual(1, 1)


class LoggingTestCase(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        logging.info(f"{self.id()}, {round(elapsed,3)}")

    def test_should_run_fast(self):
        self.assertEqual(1, 1)

    def test_should_run_slow(self):
        time.sleep(0.5)
        self.assertEqual(1, 1)
