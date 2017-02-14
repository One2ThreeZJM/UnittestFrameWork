
class myCalculator(object):
    """docstring for Calculator"""
    def addNum(self,a,b):
        return a + b

    def delNum(self,a,b):
        return a - b

    def multiNum(self,a,b):
        return a * b

    def deviNum(self,a,b):
        try:
            return a/b
        except ZeroDivisionError as e:
            return False