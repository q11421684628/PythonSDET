from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestTesterHome:
	def setup_method(self):
		'''打开浏览器之后进行登录操作，否则进不去社团'''
		self.hogwarts = webdriver.Chrome()
		self.hogwarts.maximize_window()
		self.hogwarts.get("https://testerhome.com/")
		self.hogwarts.find_element(By.LINK_TEXT, "登录").click()
		self.hogwarts.implicitly_wait(2)
		self.hogwarts.find_element(By.ID, "user_login").send_keys("1142684628@qq.com")
		self.hogwarts.find_element(By.ID, "user_password").send_keys("q1142684628")
		self.hogwarts.find_element(By.NAME, "commit").click()
		# 隐式等待
		self.hogwarts.implicitly_wait(2)

	def teardown_method(self):
		self.hogwarts.quit()

	"""课间作业1：进入testerhome，访问社团，访问霍格沃兹测试学院，访问最顶部的第一个帖子。把代码贴到回复里。"""

	def test_hogwarts(self):
		self.hogwarts.find_element(By.LINK_TEXT, "社团").click()
		# time.sleep(3)
		# 最好使用css的定位方法集，link有可能导致解析元素的时候出现异常
		element = (By.CSS_SELECTOR, "div.media-heading > a")
		# 显示等待，等待该元素可点击时再执行下一步
		WebDriverWait(self.hogwarts, 10).until(expected_conditions.element_to_be_clickable(element))
		self.hogwarts.find_element(*element).click()
		time.sleep(3)
		self.hogwarts.find_element(By.CSS_SELECTOR, ".topic:nth-child(1) .title a").click()
		time.sleep(5)

	'''作业2：进入testerhome，访问MTSC2020置顶帖，点击目录，点击议题征集范围。把代码贴到回复里，'''

	def test_MTSC2020(self):
		self.hogwarts.find_element(By.LINK_TEXT, "社区").click()
		self.hogwarts.implicitly_wait(3)
		self.hogwarts.find_element(By.PARTIAL_LINK_TEXT, "MTSC").click()
		self.hogwarts.implicitly_wait(3)
		self.hogwarts.find_element(By.CSS_SELECTOR, ".markdown-toc > div > button").click()
		self.hogwarts.implicitly_wait(3)
		self.hogwarts.find_element(By.CSS_SELECTOR, ".markdown-toc > div > div  ul > li:nth-child(4) > a").click()
		time.sleep(6)

class TestAddPeople:
	'''课后作业3：企业微信自动添加成员，需要复用已经登录的chrome，需要debugger address，代码贴到回复里'''

	def setup_method(self):
		options = webdriver.ChromeOptions()
		options.debugger_address = "localhost:8080"
		self.add_people = webdriver.Chrome(options=options)
		self.add_people.get("https://work.weixin.qq.com/wework_admin/frame#index")

	@pytest.mark.parametrize("name,acctid,mobile", {
		("test_addPeople","test_addPeople","13928394839")
	})
	def test_addPeople(self, name, acctid, mobile):
		'''设置显示等待该元素可被点击'''
		element = (By.LINK_TEXT, "添加成员")
		WebDriverWait(self.add_people, 5).until(expected_conditions.element_to_be_clickable(element))
		self.add_people.find_element(*element).click()
		name_element = (By.NAME, "username")
		WebDriverWait(self.add_people, 3).until(expected_conditions.visibility_of_element_located(name_element))
		self.add_people.find_element(By.NAME, "username").send_keys(name)
		self.add_people.find_element(By.NAME, "acctid").send_keys(acctid)
		self.add_people.find_element(By.NAME, "mobile").send_keys(mobile)
		self.add_people.find_element(By.CSS_SELECTOR, "div:nth-child(3) > a.qui_btn.ww_btn.js_btn_save").click()
		member = (By.ID, "member_list")
		WebDriverWait(self.add_people, 5).until(expected_conditions.visibility_of_element_located(member))
		a = len(self.add_people.find_elements(By.CSS_SELECTOR, "[title='test_addPeople']"))
		assert a == 1