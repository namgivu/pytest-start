import unittest, sys

from service.hash     import md5
from service.parallel import get_current_process_thread_id
from service.postgres import PostgresSvc
from service.postgres import user, pswd, host, port


def tid(self): # tid aka. test id, self is the :self inside a test method
    return unittest.TestCase.id(self)


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
