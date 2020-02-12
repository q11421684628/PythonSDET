from selenium.webdriver.common.by import By

from PageObjectLianXi.POwork.page.addressbook_page import AddressBook
from PageObjectLianXi.POwork.page.base_page import BasePage

class Main(BasePage):
	def add_people(self):
		self._driver.find_element(By.LINK_TEXT, "添加成员").click()
		return AddressBook(self._driver)