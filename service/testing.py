import unittest


def tid(self): # tid aka. test id
    return unittest.TestCase.id(self)
