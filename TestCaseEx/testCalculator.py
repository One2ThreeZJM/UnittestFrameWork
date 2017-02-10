# import sys
# sys.path.append("..")

import unittest
from SourceCode.Calculator import Calculator
from ddt import data, file_data, unpack,ddt
from common import common

path='TestData/'

@ddt
class TestCalculator(unittest.TestCase):
    """docstring for TestAdd"""

    @data(*common.getCsv(path+'testadd.csv'))
    @unpack
    def testAdd(self,a,b,result):
        '''testAdd'''
        self.assertEqual(Calculator.addNum(self,float(a),float(b)),float(result))
        print(result)

    @data(*common.getCsv(path+'testdel.csv'))
    @unpack
    def testDel(self,a,b,result):
        '''testDel'''
        self.assertEqual(Calculator.delNum(self,float(a),float(b)),float(result))

    @data(*common.getCsv(path+'testmult.csv'))
    @unpack
    def testNult(self,a,b,result):
        '''testNult'''
        self.assertEqual(Calculator.multiNum(self,float(a),float(b)),float(result))

    @data(*common.getCsv(path+'testdevi.csv'))
    @unpack
    def testdevi(self,a,b,result):
        '''testdevi'''
        if Calculator.deviNum(self,float(a),float(b))==False:
            isTrue = result==bool(result)
            self.assertEqual(Calculator.deviNum(self,float(a),float(b)),isTrue)
        else:
            self.assertEqual(Calculator.deviNum(self,float(a),float(b)),float(result))


if __name__ == '__main__':
    unittest.main()
        