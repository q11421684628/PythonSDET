from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from logger import Log


class BasePage:
    log = Log()
    _back_list = [
        (By.ID, "tv_agree"),
        (By.XPATH, '//*[@text="确定"]'),
        (By.ID, "image_cancel"),
        (By.XPATH, '//*[@text="下次再说"]')
    ]
    _error_min = 0
    _error_max = 3

    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # todo:当有广告、评价等各种弹框出现的时候，要进行异常流程处理
    def find(self, locator, value: str = None):
        self.log.info(locator)
        self.log.info(value)
        try:
            # 寻找控件
            elemen = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
                locator, value)
            # 如果寻找成功，清空错误次数
            self._error_min = 0
            return elemen
        except Exception as e:
            # 如何错误次数达到上限就抛出错误
            if self._error_min > self._error_max:
                raise e
            # 记录一直报错的异常次数
            self._error_min += 1
            # 对黑名单进行处理
            for element in self._back_list:
                self.log.info(element)
                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(locator, value)
            # 如果黑名单也没有，直接抛出错误
            self.log.warning("back list not one found")
            raise e

    # todo:同样异常，通过装饰器让函数自动处理异常
    def find_and_get_text(self, locator, value: str = None):
        self.log.info(locator)
        self.log.info(value)
        try:
            # 寻找控件
            elemen = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
                locator, value)
            # 如果寻找成功，清空错误次数
            self._error_min = 0
            return elemen.text
        except Exception as e:
            # 如何错误次数达到上限就抛出错误
            if self._error_min > self._error_max:
                raise e
            # 记录一直报错的异常次数
            self._error_min += 1
            # 对黑名单进行处理
            for element in self._back_list:
                self.log.info(element)
                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find_and_get_text(locator, value)
            # 如果黑名单也没有，直接抛出错误
            self.log.warning("back list not one found")
            raise e

    def text(self, key):
        return (By.XPATH, '//*[@text="%s"]' % key)

    def find_by_text(self, key):
        return self.find(self.text(key))
