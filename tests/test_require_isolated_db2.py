import unittest

from service          import testing
from service.postgres import PostgresSvc
from model.user       import User


def setUpModule():    pass # nothing here for now
def tearDownModule(): pass # nothing here for now


class TestRequireIsolatedDbParallel(unittest.TestCase):

    def setUp(self):    pass # nothing here for now
    def tearDown(self): pass # nothing here for now


    @testing.isolate_db
    def test_require_isolated_db1(self):
        u_all = User.find_all()
        assert len(u_all) == 0


    @testing.isolate_db
    def test_require_isolated_db2(self):
        # create fixture
        u1 = User.create(dict(email='some@e.mail1'))
        u2 = User.create(dict(email='some@e.mail2'))
        PostgresSvc.insert(u1)
        PostgresSvc.insert(u2)

        # check rows count
        u_all = User.find_all()
        assert len(u_all) == 2
