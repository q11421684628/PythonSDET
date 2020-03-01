"""Appium进阶"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from logger import Log


class TestApiDemo:
    log = Log()

    def setup(self):
        caps = {}
        caps["platformName"] = "android"  # 移动端类型，Android、IOS
        caps["deviceName"] = "appium-test"  # 设备名，可随意填写
        caps["appPackage"] = "io.appium.android.apis"  # app包名
        # app入口 win系统可使用 adb shell "logcat | grep -i displayed"查看
        caps["appActivity"] = ".ApiDemos"
        # caps["noReset"] = True  # 是否在测试前后重置相关环境
        # caps["dontStopAppOnReset"] = True  # 如果启动了App那么就不重启App应用，便于调试加快速度
        # caps["reseKeyboard"] = True  # 测试完成之后重置输入法，需与上面那个参数一起使用
        # caps["unicodeKeyboard"] = True  # 允许非英文之外的格式输入
        caps["skipServerInstallation"] = True  # 如果安装过uiAutomator2就跳过安装，进一步加快速度

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_scroll(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Views' and contains(@resource-id, 'text')]").click()
        size = self.driver.get_window_size()
        width = size["width"]
        height = size["height"]
        """通过while循环遍历页面是否有该元素出现，若没有的话就滚动屏幕"""
        i = 0
        while True:
            try:
                self.driver.find_element(
                    MobileBy.XPATH, "//*[@text='Popup Menu' and contains(@resource-id, 'text1')]").click()
                break
            except Exception:
                TouchAction(self.driver).long_press(x=width * 0.5, y=height * 0.8)\
                    .move_to(x=width * 0.5, y=height * 0.2).release().perform()
                # self.driver.swipe(width / 2, height * 0.8, width / 2, height * 0.2)
                i = i + 1
                self.log.info("元素找不到，正在第%d次滚动屏幕" % i)

        self.driver.find_element(MobileBy.XPATH, "//*[@text='Make a Popup!']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Search' and contains(@resource-id, 'title')]").click()
        # 通过uiautomator2给Tast给定的一个临时class名来获取Toast的Xpath路径
        Toast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert "Search" in Toast



    def teardown(self):
        pass
