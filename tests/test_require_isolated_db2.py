import unittest

from service          import testing
from service.hash     import md5
from service.postgres import PostgresSvc
from model.user       import User


def setUpModule():    pass # nothing here for now
def tearDownModule(): pass # nothing here for now


class TestRequireIsolatedDbParallel(unittest.TestCase):
    """
    we redo tests in :TestRequireIsolatedDb here making it parallel-compatible
    """

    def setUp(self):
        self.test_id = testing.tid(self)
    
    def tearDown(self): pass


    def test_require_isolated_db1(self):
        # set up
        #TODO create decorator to do the below block
        _, engine, _ = testing.require_isolated_db(self.test_id)
        PostgresSvc.create_db(db_name=md5(self.test_id))
        PostgresSvc.create_all_postgres_tables(engine)
        self.addCleanup(PostgresSvc.drop_db, db_name=md5(self.test_id)) #TODO can we have code to queue this to execute when test ends?

        # main test
        u_all = User.find_all()
        assert len(u_all) == 0


    def test_require_isolated_db2(self):
        # set up & tear down
        #TODO create decorator to do the below block
        _, engine, _ = testing.require_isolated_db(self.test_id)
        PostgresSvc.create_db(db_name=md5(self.test_id))
        PostgresSvc.create_all_postgres_tables(engine)
        self.addCleanup(PostgresSvc.drop_db, db_name=md5(self.test_id)) #TODO can we have code to queue this to execute when test ends?

        # create fixture
        u1 = User.create(dict(email='some@e.mail1'))
        u2 = User.create(dict(email='some@e.mail2'))
        PostgresSvc.insert(u1)
        PostgresSvc.insert(u2)

        # check rows count
        u_all = User.find_all()
        assert len(u_all) == 2
