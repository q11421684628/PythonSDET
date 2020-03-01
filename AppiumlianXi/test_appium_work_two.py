from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

@allure.epic("雪球App测试")
@allure.feature("webview测试")
class TestWebview:
    def setup(self):
        webviews = {
            "platformName": "android",
            "deviceName": "OPPO-A57",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            "reseKeyboard": True,
            "unicodeKeyboard": True,
            "skipServerInstallation": True,
            "chromedriverExecutable": r"E:\PythonSDET\chromedriver\chromedriver_2.20.exe"
            # 当多台设备同时开启时，需要指定某台设备运行的话需要udid参数，否则会一直运行adb devices命令下的第一台设备
            # "udid":"emulator-5554"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", webviews)
        self.driver.implicitly_wait(10)

    @allure.title("港美股webview测试")
    def test_hk_stocks_kh(self):
        """点击交易页面的港美股，跳转到webview页面输入手机号和验证码之后返回到交易页面"""
        trading = (By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]")
        # 显式等待交易按钮可点击
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(trading))
        self.driver.find_element(*trading).click()
        # 显式等待上下文大于1时切换到最后一个上下文中
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.contexts) > 1)
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 点击港美股按钮
        self.driver.find_element(By.CSS_SELECTOR, ".trade_home_xueying_SJY").click()
        # 显示等待window窗口大于1时切换到最后一个窗口
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 显示等待手机输入栏出现时输入手机号和验证码
        phone = (By.CSS_SELECTOR, "[maxlength='11']")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(phone))
        self.driver.find_element(*phone).send_keys("13928394028")
        code = (By.CSS_SELECTOR, "[maxlength='6']")
        self.driver.find_element(*code).send_keys("123456")
        # 点击立即开户按钮，校验是否有toast出现
        self.driver.find_element(By.CSS_SELECTOR, ".open_form-submit_1Ms").click()
        Toast = self.driver.find_element(By.CSS_SELECTOR, ".Toast_toast_22U").text
        assert "发送验证" in Toast
        # 切换回第一个窗口的上下文，点击返回按钮
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.switch_to.context(self.driver.contexts[0])
        self.driver.find_element(By.ID, "action_bar_back").click()
        # 断言是否返回到交易页面
        deal = self.driver.find_element(*trading).text
        assert "交易" in deal
