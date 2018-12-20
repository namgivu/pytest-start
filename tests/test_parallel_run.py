import time
import unittest

def setUpModule():    pass # nothing here for now
def tearDownModule(): pass # nothing here for now


class TestParallelRun(unittest.TestCase):

    def setUp(self):    pass # nothing here for now
    def tearDown(self): pass # nothing here for now


    def test_parallel_run1(self):
        time.sleep(5)


    def test_parallel_run2(self):
        time.sleep(5)
