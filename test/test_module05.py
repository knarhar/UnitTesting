import unittest


def setUpModule():  # module-level fixture, executed before any method in the test module
    """called once, before anything else in this module"""
    print("In setUpModule()...")


def tearDownModule():  # module-level fixture, executed after all methods in the test module
    """called once, after everything else in this module"""
    print("In tearDownModule()...")


class TestClass06(unittest.TestCase):
    @classmethod  # The @classmethod decorator must have a reference to a class object as the first parameter
    def setUpClass(cls):  # class-level fixture, executed before any method in the test class
        """called once, before any test"""
        print("In setUpClass()...")

    @classmethod
    def tearDownClass(cls):  # class-level fixture, executed after all methods in the test class
        """called once, after all tests, if setUpClass
        successful"""
        print("In tearDownClass()...")

    def setUp(self):  # method-level fixture, executed before and after every test method in the test class
        """called multiple times, before every test method"""
        print("\nIn setUp()...")

    def tearDown(self):  # method-level fixture, executed before and after every test method in the test class
        """called multiple times, after every test method"""
        print("\nIn tearDown()...")

    def test_case01(self):
        self.assertTrue("PYTHON".isupper())
        print("\nIn test_case01()")

    def test_case02(self):
        self.assertFalse("python".isupper())
        print("\nIn test_case02()")


if __name__ == ' main ':
    unittest.main(verbosity=2)

'''
    Test fixtures are the set of steps performed before and after tests
'''