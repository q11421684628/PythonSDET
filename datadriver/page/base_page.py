from selenium.webdriver.android.webdriver import WebDriver

def exception_handle(fun):
    def magic(*args, **kwargs):
        _self: BasePage = args[0]  # 因为self是非常特殊的，有些时候会用到，所以需要将self重新定义
        try:
            result = fun(*args, **kwargs)  # 不管传的是什么函数，都会直接调用那个函数，*args和**kwargs代表函数内的任意参数
            # 清空错误次数
            _self._error_count = 0
            return result
        except Exception as e:
            # 如果次数太多，就退出异常逻辑，直接报错
            if _self._error_count > _self._error_max:
                raise e
            # 记录一直异常的次数
            _self._error_count += 1
            # 对黑名单里的弹框进行处理
            for element in _self._back_list:
                elements = _self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    # 继续寻找原来的正常控件
                    return magic(*args, **kwargs)
            # 如果黑名单也没有，直接报错
            raise e


class BasePage:
    _back_list = []
    _error_count = 0
    _error_max = len(_back_list)

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @exception_handle
    def find(self, locator, value: str = None):
        if isinstance(locator, tuple):
            return self._driver.find_element(*locator)
        else:
            return self._driver.find_element(locator, value)
    
    @exception_handle
    def find_and_get_text(self, locator, value: str = None):
        return self.find(locator, value).text