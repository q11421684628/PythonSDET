from appium.webdriver.common.mobileby import MobileBy
from po_appium.page.base_page import BasePage

class Search(BasePage):
	#todo:多平台、多版本、多个可能定位符
	_name = (MobileBy.ID, "name")
	def search(self, key: str):
		self.find(MobileBy.ID, "search_input_text").send_keys(key)
		element = self._name
		self.find(element).click()
		return self

	def get_prices(self, key: str) -> float:
		return  float(self.find(MobileBy.ID, "current_price").text)
