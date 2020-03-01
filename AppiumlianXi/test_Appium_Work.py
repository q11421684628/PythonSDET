from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.epic("雪球增加和查询自选股票")
class TestAppiumWork:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"  # 移动端类型，Android、IOS
        caps["deviceName"] = "appium-test"  # 设备名，可随意填写
        caps["appPackage"] = "com.xueqiu.android"  # app包名
        # app入口 win系统可使用 adb shell "logcat | grep -i displayed"查看
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True  # 是否在测试前后重置相关环境
        caps["dontStopAppOnReset"] = True  # 如果启动了App那么就不重启App应用，便于调试加快速度
        caps["unicodeKeyboard"] = True  # 允许非英文之外的格式输入
        caps["reseKeyboard"] = True  # 测试完成之后重置输入法，需与上面那个参数一起使用
        caps["skipServerInstallation"] = True  # 如果安装过uiAutomator2就跳过安装，进一步加快速度

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    @allure.title("作业2：搜索在香港上市的阿里巴巴的股票市价")
    def test_search_and_get_price_from_hk(self):
        """点击搜索栏并输入搜索数据之后点击搜索结果的第一行数据之后跳转到股票页面获取目前股价"""
        self.driver.find_element(MobileBy.ID, "home_search").click()
        self.driver.find_element(
            MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        stock = (MobileBy.XPATH, "//*[contains(@resource-id, 'title_container')]//*[@text='股票']")
        self.driver.find_element(*stock).click()
        price = self.driver.find_element(
            By.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id, 'current_price')]"
        ).text
        assert float(price) < 219

    def search_stock(self):
        action_close = (By.XPATH, "//*[contains(@resource-id, 'action_close')]")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(action_close))
        self.driver.find_element(*action_close).click()
        self.driver.find_element(MobileBy.ID, "home_search").click()
        self.driver.find_element(
            MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        search_added_stock = (By.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id, 'followed_bt')]")
        text = self.driver.find_element(*search_added_stock).get_attribute("resource-id")
        assert "followed_btn" in text

    @allure.title("作业3：添加某只股票到自选，然后再次搜索并验证，股票已经加入自选。（不要使用文字内容判断，使用get attribute）")
    def test_search_and_add_stock(self):
        self.driver.find_element(MobileBy.ID, "home_search").click()
        self.driver.find_element(
            MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        stock = (MobileBy.XPATH, "//*[contains(@resource-id, 'title_container')]//*[@text='股票']")
        self.driver.find_element(*stock).click()
        """点击自选按钮添加自选"""
        add_stock = (
            By.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id, 'add_attention')]//*[@text='加自选']")
        self.driver.find_element(*add_stock).click()
        """判断是否有弹出框，没有的话直接执行search_stock方法。（第一次添加自选时会有弹出框）"""
        click_bth = (By.XPATH, "//*[contains(@resource-id, 'll_bottom_button')]//*[@text='下次再说']")
        if WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located(click_bth)):
            self.search_stock()
        else:
            self.driver.find_element(*click_bth).click()
            self.search_stock()

    def teardown(self):
        """在每个方法结束时判断是否在首页，避免出现测试用例失败"""
        home_page = (By.XPATH, "//*[@text='我的']")
        if WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(home_page)):
            self.driver.find_element(By.XPATH, "//*[contains(@resource-id, 'action_close')]").click()
