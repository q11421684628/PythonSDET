from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from po_appium.page.base_page import BasePage

class Search(BasePage):
	#todo:多平台、多版本、多个可能定位符
	_name = (MobileBy.ID, "name")
	def search(self, key: str):
		# self.find(MobileBy.ID, "search_input_text").send_keys(key)
		# self.find(self._name).click()
		self._params={}
		self._params["key"] = key
		self.steps("../page/search.yaml")
		return self

	def get_prices(self, key: str) -> float:
		return  float(self.find(MobileBy.ID, "current_price").text)

	def add_select(self):
		element = self.find_by_text("加自选")
		element.click()
		return self
	def get_msg(self):
		return self.find_and_get_text(By.ID, "followed_btn")

	"""点击返回按钮，返回行情界面"""
	def back_stocks(self):
		return self.find(By.ID, "action_close").click()