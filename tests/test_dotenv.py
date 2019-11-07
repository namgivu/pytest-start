import os
import unittest


def setUpModule():    pass   # nothing here for now
def tearDownModule(): pass   # nothing here for now


class TestLoadEnv(unittest.TestCase):

    def setUp(self):    pass   # nothing here for now
    def tearDown(self): pass   # nothing here for now


    def test(self):
        DB_HOST = os.environ.get('DB_HOST')
        assert DB_HOST == "foobarbaz"
