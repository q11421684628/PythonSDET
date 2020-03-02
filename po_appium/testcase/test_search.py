import pytest

from po_appium.page.app import App

class TestSearch:
	def setup(self):
		self.main = App().start().main()

	def test_search(self):
		assert self.main.goto_search_page().search("alibaba").get_prices("BABA") > 200

	@pytest.mark.parametrize("key, stock_type, price",[
		("alibaba", "BABA", 200),
		("JD", "JD", 20)
	])
	def test_search_data(self, key, stock_type, price):
		assert self.main.goto_search_page().search(key).get_prices(stock_type) > price