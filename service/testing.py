import unittest, sys

from service.hash     import md5
from service.parallel import get_current_process_thread_id
from service.postgres import PostgresSvc
from service.postgres import user, pswd, host, port


def tid(self): # tid aka. test id, self is the :self inside a test method
    return unittest.TestCase.id(self)


#region @isolate_db for test method
"""
this decorator used to mark a test method that an isolated db is required to run it
"""

def require_isolated_db(test_id):
    """
    This method is called by a test method which means we need to create an isolated database for that test - db name to be the test id
    """

    # register :test_id
    sys.require_isolated_db[get_current_process_thread_id()] = test_id

    # create session for :test_id
    db                                 = md5(test_id) # we hash to make a short db name since postgres has limited db name length
    Session, engine, connection_string = PostgresSvc.make_session(user, pswd, host, port, db)
    sys.test_sessions[test_id]         = Session, engine, connection_string

    return Session, engine, connection_string


def isolate_db(wrapped_f): # wrapped_f aka. wrapped function # creating python decorator ref. https://www.learnpython.org/en/Decorators

    def wrapper_f(*args, **kwargs):
        self         = args[0]
        test_id      = tid(self)
        _, engine, _ = require_isolated_db(test_id)
        db_name      = md5(test_id)

        PostgresSvc.create_db(db_name)
        PostgresSvc.create_all_postgres_tables(engine)

        self.addCleanup(PostgresSvc.drop_db, db_name)

        wrapped_f(*args, **kwargs)

    return wrapper_f

#endregion @isolate_db for test method
