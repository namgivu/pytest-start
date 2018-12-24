import unittest

from service.postgres import PostgresSvc
from model.user       import User

"""
CAUTION
This test class works only when running it NON-PARALLEL
pytest -x  # WITH NO -n option here

The filename has prefix _ to hide from pytest run
We keep this file as a proof to show parallel-not-compatible test
"""

def setUpModule():    pass # nothing here for now
def tearDownModule(): pass # nothing here for now


class TestRequireIsolatedDb(unittest.TestCase):

    def setUp(self):
        PostgresSvc.create_db(db_name='test')
        PostgresSvc.create_all_postgres_tables()

    def tearDown(self):
        PostgresSvc.drop_all_postgres_tables()


    def test_require_isolated_db1(self):
        """
        here, we create empty :user
        """
        u_all = User.find_all()
        assert len(u_all) == 0


    def test_require_isolated_db2(self):
        """
        here, we create :user with some row(s)
        """

        # create fixture
        u1 = User.create(dict(email='some@e.mail1'))
        u2 = User.create(dict(email='some@e.mail2'))
        PostgresSvc.insert(u1)
        PostgresSvc.insert(u2)

        # check rows count
        u_all = User.find_all()
        assert len(u_all) == 2
