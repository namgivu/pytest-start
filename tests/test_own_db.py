import unittest
import service.testing

def setUpModule():    pass # nothing here for now
def tearDownModule(): pass # nothing here for now


class TestOwnDb(unittest.TestCase):

    def tid(self):
        return unittest.TestCase.id(self)


    def setUp(self):
        service.testing.set_up_db(self.tid())

    def tearDown(self):
        service.testing.tear_down_db(self.tid())


    def test_own_db(self):
        abb = 122
