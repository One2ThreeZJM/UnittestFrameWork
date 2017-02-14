import unittest
from TestCaseEx.testCalculator import TestCalculator
from common import HTMLTestRunner

path = './TestCaseEx'   

if __name__ == '__main__':
    
    #找到目录下所有'test*.py'的文件,并且加载到TestSuite
    discover = unittest.defaultTestLoader.discover(path, pattern='test*.py')
    runner=unittest.TextTestRunner(verbosity=2)
    testresult = runner.run(discover)
    # print(dir(testresult))
    # print('testsRun:',testresult.testsRun)
    # print('failures',len(testresult.failures))
    # print('errors',testresult.errors)

    

    # #TextTestRunner结果输出到文件
    # discover = unittest.defaultTestLoader.discover(path, pattern='test*.py')
    # log_file = "log_file.txt"
    # with open(log_file,'w') as f:
    #     #默认值是1，调试用2
    #     runner=unittest.TextTestRunner(verbosity=2,stream=f)
    #     runner.run(discover)

    # ----------------------------------------------------------------------
    #因为使用ddt，所以创建类时自动创建方法名，因此不能直接使用TestCalculator('testAdd')
    #所以要结合getTestCaseNames方法使用
    # names= unittest.getTestCaseNames(TestCalculator,'test')
    # test_suite = unittest.TestSuite()
    # test_suite.addTest(TestCalculator('testAdd_1___1____1____2__'))
    # test_runner = unittest.TextTestRunner()
    # test_runner.run(test_suite)

    # ----------------------------------------------------------------------
    # 运行测试套中包含的用例，将结果保存到result参数对应的TestResult对象中
    # discover = unittest.defaultTestLoader.discover(path, pattern='test*.py')
    # r = unittest.TestResult()
    # discover.run(r)
    # print(r)
    # print(discover.countTestCases())
    

    # ----------------------------------------------------------------------
    #使用HTMLTestRunner 生成报告
    # discover = unittest.defaultTestLoader.discover(path, pattern='test*.py')
    # with open('my_report.html', 'wb') as fp:
    #     runner = HTMLTestRunner.HTMLTestRunner(
    #                 stream=fp,
    #                 title='My unit test',
    #                 description='This demonstrates the report output by HTMLTestRunner.'
    #                 )
    #     runner.run(discover)
