# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from logger import Log


class TestXueqiu:
    log = Log()

    def setup(self):
        caps = {}
        caps["platformName"] = "android"  # 移动端类型，Android、IOS
        caps["deviceName"] = "192.168.185.102:5555"  # 设备名，可随意填写
        caps["appPackage"] = "com.xueqiu.android"  # app包名
        # app入口 win系统可使用 adb shell "logcat | grep -i displayed"查看
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True  # 是否在测试前后重置相关环境
        # caps["dontStopAppOnReset"] = True  # 如果启动了App那么就不重启App应用，便于调试加快速度
        caps["reseKeyboard"] = True  # 测试完成之后重置输入法，需与上面那个参数一起使用
        caps["unicodeKeyboard"] = True  # 允许非英文之外的格式输入
        caps["skipServerInstallation"] = True  # 如果安装过uiAutomator2就跳过安装，进一步加快速度
        # caps["chromedriverExecutableDir"] = "E:\PythonSDET\chromedriver_win32" #指定一个webdriver的存放目录
        caps["chromedriverExecutable"] = r"E:\PythonSDET\chromedriver\chromedriver_2.20.exe" #强行指定目录下的某个版本
        # caps["chromedriverChromeMappingFile"] = "./webdriver.json"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_search(self):
        # el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        # el1.click()
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        # el2 = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        # el2.click()
        self.driver.find_element(MobileBy.ID, "home_search").click()
        # el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        # el3.send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")

    def test_search_and_get_price(self):
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.ID, "home_search").click()
        self.driver.find_element(
            MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        price = self.driver.find_element(MobileBy.ID, "current_price").text
        assert float(price) > 200

    # 滚动屏幕至某元素出现，另一种写法是使用AndroidUIAutomator，但该方法只适用于安卓端
    def test_scroll(self):
        size = self.driver.get_window_size()
        width = size["width"]
        height = size["height"]
        """通过while循环遍历页面是否有该元素出现，若没有的话就滚动屏幕"""
        i = 0
        while True:
            try:
                self.driver.find_element(
                    MobileBy.XPATH, "//*[@text='1小时前' and contains(@resource-id, 'created_at')]").click()
                break
            except Exception:
                self.driver.swipe(width / 2, height * 0.8, width / 2, height * 0.2)
                i = i + 1
                self.log.info("元素找不到，正在第%d次滚动屏幕" % i)

    def test_device(self):
        """系统级别的操作，切入后台5秒，锁屏5秒之后解锁"""
        self.driver.background_app(5)
        self.driver.lock(5) \
            .unlock()  # 不能轻易在模拟器上使用，否则锁屏之后可能会解不了锁

    # 在进行webview自动化时会遇到“No Chromedriver found that can automate Chrome”的报错，原因是因为webview的浏览器的驱动没有下载，
    # 需要去到https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/web/chromedriver.md查看对应的浏览器版本
    # 的驱动进行下载，下载之后可以在配置项增加“chromedriverExecutableDir”参数来指定一个存放所有版本的webdriver的目录。但是该参数有
    # 两个问题：一、只支持单级目录，多级目录不支持；二、必须满足浏览器版本的webdriver（例如浏览器版本为44.0.2403，那么webdriver对应的
    # 版本必须等于44.0.2403，不能根据webdriver所能支持的最低版本来判断。目前有两个办法解决：一个是使用“chromedriverExecutable”参数
    # 强行指定一个版本，缺点是多个手机会有多个不同的版本；另一个办法是使用“chromedriverChromeMappingFile”参数，该参数指定一个目录
    # 下的json文件，该文件采用字典键值对的形式强行将webdriver的版本与浏览器的版本匹配上，缺点是匹配速度有点慢
    def test_webview_context(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()
        # 首次做测试的时候，用于分析上下文
        # for i in range(5):
        #     print(self.driver.contexts)
        #     time.sleep(1)
        # print(self.driver.page_source)
        # 坑1：webview上下文的出现，大概有3s的延迟
        WebDriverWait(self.driver, 10).until(lambda x: len(self.driver.contexts) > 1)
        # 坑2：chromedriver的版本必须与chrome版本必须对应
        # 坑3：chromedriver可能会存在无法对应chrome版本的情况，需要使用caps的mapping file或者chromedriverExecutable直接匹配版本
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 使用chrome inspect分析界面控件，需要代理，需要chrome62及以前的版本，62以上有bug
        self.driver.find_element(By.CSS_SELECTOR, ".trade_home_info_3aI").click()
        # 首次做测试的时候，用来分析窗口
        # for i in range(5):
        #     print(self.driver.window_handles)
        #     time.sleep(1)
        # 坑4：可能会出现多窗口，要注意切换
        WebDriverWait(self.driver, 10).until(lambda x: len(self.driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        phone = (By.ID, "phone-number")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(phone))
        self.driver.find_element(*phone).send_keys("123456")

    def teardown(self):
        pass
# time.sleep(10)
# self.driver.quit()
