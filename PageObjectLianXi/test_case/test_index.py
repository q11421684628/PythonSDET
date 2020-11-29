
from PageObjectLianXi.page.index import Index

class TestIndex:
	def setup(self):
		self.index = Index()

	def test_register(self):
		# self.driver.find_element(By.LINK_TEXT, "立即注册").click()
		# self.driver.find_element(By.ID, "corp_name").send_keys("1233")
		# self.driver.find_element(By.ID, "iagree").click()
		# self.driver.find_element(By.ID, "submit_btn").click()
		self.index.goto_register().register("123456")

	def test_login(self):
		register_page = self.index.goto_login().goto_registry().register("测吧有限公司")
		print("|".join(register_page.get_error_message()))
		assert "请选择" in " | ".join(register_page.get_error_message())

	def teardown(self):
		self.index.close()
