import unittest


def setUpModule():
    """called once, before anything else in this module"""
    print("In setUpModule()...")

def tearDownModule():
    """called once, after everything else in this module"""
    print("In tearDownModule()...")


class TestClass06(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """called once, before any test"""
        print("In setUpClass()...")

    @classmethod
    def tearDownClass(cls):
        """called once, after all tests, if setUpClass
        successful"""
        print("In tearDownClass()...")

    def setUp(self):
        """called multiple times, before every test method"""
        print("\nIn setUp()...")

    def tearDown(self):
        """called multiple times, after every test method"""
        print("In tearDown()...")

    def test_case01(self):
        self.assertTrue("PYTHON".isupper())
        print("In test_case01()")

    def test_case02(self):
        self.assertFalse("python".isupper())
        print("In test_case02()")


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestClass06))
    return test_suite


if __name__ == '__main__':
    mySuit = suite()
    runner = unittest.TextTestRunner()
    runner.run(mySuit)

'''
    This code example created a suite that created an object for unittest.TestSuite(). 
Then it added the test class to this object with the addTest() method.
You can add multiple test classes to that. You can also create multiple test suites like that.
Finally, this example is creating an object of this test suite class in the main section.
It also creates a testrunner object and then calls that object to run the object of the test suite.
You can create multiple test suites and create their objects in the main section.
Then you can use the testrunner object to call the objects of those test suites
'''