import unittest # importing unittest module


class TestClass01(unittest.TestCase):  # test class subclassed from TestCase
    def test_case01(self):  # test method
        my_str = "ASHWIN"
        my_int = 999

        self.assertTrue(isinstance(my_str, str))  # assertion methods that check if the argument passed is True or False
        self.assertTrue(isinstance(my_int, int))

    def test_case02(self):  # test method
        my_pi = 3.14

        self.assertFalse(isinstance(my_pi, int))


if __name__ == '__main__':
    unittest.main()


'''
    If the argument meets the assert condition, the test case passes otherwise, it fails. unittest.main() - test runner
'''