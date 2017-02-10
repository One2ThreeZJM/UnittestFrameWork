import unittest
from TestCaseEx.testCalculator import TestCalculator
 
path = './TestCaseEx'   

if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover(path, pattern='test*.py')
    runner=unittest.TextTestRunner()
    runner.run(discover)
   