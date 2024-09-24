import unittest


class TestClass14(unittest.TestCase):
    def test_case01(self):
        raise Exception


'''
    When an exception is raised in a test case, the test case fails. 
    This code raises Exception explicitly.
    The failure message shown when the test fails due to an exception is
different from when the test fails due to an assertion.
''' 