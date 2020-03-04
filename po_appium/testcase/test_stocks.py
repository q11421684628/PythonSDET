from po_appium.page.app import App

class TestStocks:
	def setup(self):
		self.stocks = App().start().main()

	def test_search_by_back(self):
		"""从行情界面点击搜素图标进搜索界面搜索股票添加为自选之后返回行情界面"""
		self.stocks.goto_stocks().goto_search_page().search("bilibili").add_select().back_stocks()
		assert "自选股" in self.stocks.goto_stocks().get_current_title()