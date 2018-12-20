from service          import testing
from service.postgres import PostgresSvc
from tests.test_require_isolated_db import TestRequireIsolatedDb


def setUpModule():    pass # nothing here for now
def tearDownModule(): pass # nothing here for now


class TestRequireIsolatedDbParallel(TestRequireIsolatedDb):
    """
    we redo tests in :TestRequireIsolatedDb here making it parallel-compatible
    """

    def setUp(self):
        PostgresSvc.create_db(db_name=testing.tid(self))
        PostgresSvc.create_all_postgres_tables()

    def tearDown(self):
        PostgresSvc.drop_all_postgres_tables()
        PostgresSvc.drop_db(db_name=testing.tid(self))
