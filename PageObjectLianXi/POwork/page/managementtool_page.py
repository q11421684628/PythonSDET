import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjectLianXi.POwork.page.base_page import BasePage

class ManagementTool(BasePage):
	def add_images(self, path=None):
		self._driver.find_element(By.LINK_TEXT, "管理工具").click()
		"""定位素材库按钮并进行点击"""
		Material = (By.CSS_SELECTOR, "li:nth-child(5)")
		WebDriverWait(self._driver, 5).until(expected_conditions.visibility_of_element_located(Material))
		self._driver.find_element(*Material).click()
		self._driver.find_element(By.LINK_TEXT, "图片").click()
		# 点击添加图片按钮，并输入文件路径
		self._driver.find_element(By.CSS_SELECTOR, ".js_upload_file_selector").click()
		self._driver.find_element(By.CSS_SELECTOR, "#js_upload_input").send_keys(path)
		# 以图片列表有值作为判断是否上传成功
		images_list = (By.CSS_SELECTOR, ".material_pic_list_item")
		WebDriverWait(self._driver, 5).until(expected_conditions.visibility_of_element_located(images_list))
		# sudo:暂时只能通过死等来解决操作过快点击不了完成按钮问题
		time.sleep(3)
		self._driver.find_element(By.LINK_TEXT, "完成").click()
		return self._driver
