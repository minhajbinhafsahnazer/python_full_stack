class MathUtils:
    @staticmethod
    def calculateSum(array):
        return sum(array)

array = [1,2,3,4,5,6,7,8]
result = MathUtils.calculateSum(array)  #result_variable = classname.methodname(listvariable)
print(result)