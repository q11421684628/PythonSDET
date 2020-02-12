import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjectLianXi.POwork.page.base_page import BasePage

class AddressBook(BasePage):
	def add_people(self, name, acctid, mobile):
		# 通过显示等待姓名来确定是否已跳转到添加用户页
		name1 = (By.ID, "username")
		WebDriverWait(self._driver, 5).until(expected_conditions.visibility_of_element_located(name1))
		# 将输入的姓名和账号、手机参数化
		self._driver.find_element(*name1).send_keys(name)
		self._driver.find_element(By.NAME, "acctid").send_keys(acctid)
		self._driver.find_element(By.NAME, "mobile").send_keys(mobile)
		self._driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > a.js_btn_save").click()
		# 获取用户列表的值来断言是否添加成功
		member_list = len(self._driver.find_elements(By.CSS_SELECTOR, "#member_list > tr"))
		assert member_list > 1

	def editor_people(self, name, mobile):
		# 点击姓名来进入个人信息页面，并且通过显示等待编辑按钮是否可点击来判断是否跳转到了个人信息页面
		self._driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2)").click()
		editor = (By.LINK_TEXT, "编辑")
		WebDriverWait(self._driver, 5).until(expected_conditions.element_to_be_clickable(editor))
		self._driver.find_element(*editor).click()
		# 通过显示等待姓名栏是否加载完来判断是否进入编辑页面
		username = (By.NAME, "username")
		WebDriverWait(self._driver, 5).until(expected_conditions.visibility_of_element_located(username))
		self._driver.find_element(*username).clear()
		self._driver.find_element(*username).send_keys(name)
		self._driver.find_element(By.NAME, "mobile").clear()
		self._driver.find_element(By.NAME, "mobile").send_keys(mobile)
		self._driver.find_element(By.CSS_SELECTOR, " div:nth-child(3) > a.ww_btn_Blue").click()
		# 同样目前只能通过死等来判断是否修改成功
		time.sleep(2)
		editor_result = self._driver.find_element(By.CSS_SELECTOR, ".member_display_item_Phone").text
		assert mobile in editor_result