import pytest
import allure

'''作业1:假设有如下函数
	def div(a, b):
    return a/b
   针对该函数编写测试用例
'''

def div(a, b):
	return a / b

def test_div():
	assert div(3, 2) == 1.5
	assert div(2, 2) == 1
	assert div(6, 3) == 2

"""课后作业2：将作业1参数化并且通过allure来展示"""
@pytest.mark.parametrize("number1, number2, expectation", {
	(2, 1, 2),
})
@allure.title("整数除法测试")
def test_div_int(number1, number2, expectation):
	assert div(number1, number2) == expectation

@pytest.mark.parametrize("number3, number4, expectation1", {
	(1.2, 0.6, 2),
})
@allure.title("浮点数除法测试")
def test_div_float(number3, number4, expectation1):
	assert div(number3, number4) == expectation1

@pytest.mark.parametrize("number5, number6, expectation2", {
	(2, -2, -1.0),
})
@allure.title("负数除法测试")
def test_div_negative(number5, number6, expectation2):
	assert div(number5, number6) == expectation2

if __name__ == "__main__":
	pytest.main(["-q", "test_work_20191222.py"])
