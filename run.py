import unittest
from TestCaseEx.testCalculator import TestCalculator
 
    

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(TestCalculator('testdevi'))
    testunit.run()
    