import unittest

from service.postgres import PostgresSvc
from model.user       import User


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
        here, we create :user with 1 row
        """
        pass #TODO
