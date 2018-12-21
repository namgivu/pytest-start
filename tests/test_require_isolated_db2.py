from service          import testing
from service.postgres import PostgresSvc
from tests.test_require_isolated_db import TestRequireIsolatedDb


def setUpModule():    pass # nothing here for now
def tearDownModule(): pass # nothing here for now


def set_up(test_id):
    pass


class TestRequireIsolatedDbParallel(TestRequireIsolatedDb):
    """
    we redo tests in :TestRequireIsolatedDb here making it parallel-compatible
    """

    def setUp(self): pass
    def tearDown(self): pass


    def test_require_isolated_db1(self):
        #TODO create decorator to do the below block
        _, engine, _ = testing.require_isolated_db(testing.tid(self))
        PostgresSvc.create_db(db_name=testing.tid(self))
        PostgresSvc.create_all_postgres_tables(engine)

        super().test_require_isolated_db1()

        PostgresSvc.drop_db(db_name=testing.tid(self)) #TODO can we have code to queue this to execute when test ends?

    def test_require_isolated_db2(self):
        #TODO create decorator to do the below block
        _, engine, _ = testing.require_isolated_db(testing.tid(self))
        PostgresSvc.create_db(db_name=testing.tid(self))
        PostgresSvc.create_all_postgres_tables(engine)

        super().test_require_isolated_db2()

        PostgresSvc.drop_db(db_name=testing.tid(self)) #TODO can we have code to queue this to execute when test ends?
