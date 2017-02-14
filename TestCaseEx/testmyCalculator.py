import unittest
class BaseTestCase(unittest.TestCase):
    """测试继承"""
    def setUp(self):
        self._print = 'BaseTestCase.setUp'

    def tearDown(self):
        self._print = 'BaseTestCase.tearDown'

class TestCase1(BaseTestCase):
    """docstring for TestCase1"""
    def testfun1(self):
        pass

    def testfun2(self):
        pass

class TestCase2(BaseTestCase):
    """docstring for TestCase1"""
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
        



