import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class TestTesterHome:
    __name = "abc"

    def setup_method(self):
        '''打开浏览器之后进行登录操作，否则进不去社团'''
        chrome_capabilities={
            "browserName": "chrome",
            "version": "",
            "platform": "ANY",
        }
        self.hogwarts = webdriver.Remote("http://192.168.137.159:5001/wd/hub", desired_capabilities=chrome_capabilities)
        self.hogwarts.maximize_window()
        self.hogwarts.get("https://testerhome.com/")

    def test_login(self):
        self.hogwarts.find_element(By.LINK_TEXT, "登录").click()
        self.hogwarts.implicitly_wait(2)
        self.hogwarts.find_element(By.ID, "user_login").send_keys("1142684628@qq.com")
        self.hogwarts.find_element(By.ID, "user_password").send_keys("q1142684628")
        self.hogwarts.find_element(By.NAME, "commit").click()
        time.sleep(10)

    def teardown_method(self):
        self.hogwarts.quit()