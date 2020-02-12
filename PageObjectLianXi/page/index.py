from selenium.webdriver.common.by import By

from PageObjectLianXi.page.base_page import BasePage
from PageObjectLianXi.page.login import Login
from PageObjectLianXi.page.register import Register

class Index(BasePage):
	def goto_register(self):
		self._driver.find_element(By.LINK_TEXT, "立即注册").click()
		return Register(self._driver)

	def goto_login(self):
		self._driver.find_element(By.LINK_TEXT, "企业登录").click()
		return Login(self._driver)
