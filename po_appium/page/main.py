from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from po_appium.page.base_page import BasePage
from po_appium.page.profile import Profile
from po_appium.page.search import Search
from po_appium.page.stocks_page import Stocks

class Main(BasePage):
	def goto_search_page(self):
		self.find(MobileBy.ID, "home_search").click()
		return Search(self._driver)

	"""前往行情界面"""
	def goto_stocks(self):
		self.find(By.XPATH, "//*[@text='行情']").click()
		return Stocks(self._driver)

	def goto_trade(self):
		pass

	def goto_profile(self):
		self.find(By.XPATH, "//*[@text='我的']").click()
		return Profile(self._driver)

	def goto_messgae(self):
		pass