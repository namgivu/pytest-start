import sys


def pytest_configure(config):
    sys._called_from_test   = True # marking that we are running test

    # init the list used for :service.testing.require_isolated_db()
    sys.require_isolated_db = {} # eg. { ... 'process122_thread333': 'test_id444', ... }
    sys.test_sessions       = {} # eg. { ... 'test_id444': {'Session':..., 'engine':..., 'connection_string':... }, ... }


def pytest_unconfigure(config):
    del sys._called_from_test
