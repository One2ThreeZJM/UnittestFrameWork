import unittest
from TestCaseEx.testCalculator import TestCalculator
 
path = './TestCaseEx'   

if __name__ == '__main__':
    #找到目录下所有'test*.py'的文件,并且加载到TestSuite
    # discover = unittest.defaultTestLoader.discover(path, pattern='test*.py')
    #默认值是1，调试用2
    # runner=unittest.TextTestRunner(verbosity=2)
    # runner.run(discover)

    # ----------------------------------------------------------------------
    #因为使用ddt，所以创建类时，不能直接使用TestCalculator('testAdd')
    #因为已经被自动改名字了，所以要结合getTestCaseNames方法使用
    # names= unittest.getTestCaseNames(TestCalculator,'test')
    # test_suite = unittest.TestSuite()
    # test_suite.addTest(TestCalculator('testAdd_1___1____1____2__'))
    # test_runner = unittest.TextTestRunner()
    # test_runner.run(test_suite)

    # 运行测试套中包含的用例，将结果保存到result参数对应的TestResult对象中
    discover = unittest.defaultTestLoader.discover(path, pattern='test*.py')
    r = unittest.TestResult()
    discover.run(r)
    print(dir(discover))
    print(r)
    print(discover.countTestCases())
