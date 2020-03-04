from selenium.webdriver.common.by import By

from po_appium.page.base_page import BasePage
from po_appium.page.search import Search

class Stocks(BasePage):
	"""从行情页点击搜索图标"""
	def goto_search_page(self):
		self.find(By.ID, "action_search").click()
		return Search(self._driver)

	"""获取当前页面是否是自选股用来辅助断言"""
	def get_current_title(self):
		return self.find(By.ID, "title_text").text
