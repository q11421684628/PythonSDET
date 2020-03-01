import time

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
	def __init__(self, driver:WebDriver=None):
		'''"C:\Program Files (x86)\Google\Chrome\Application\Chrome" --remote-debugging-port=9222
			使用该命令可以在当前浏览器器打开地址'''
		if driver is None:
			options = webdriver.ChromeOptions()
			options.debugger_address = "localhost:9222"
			self._driver = webdriver.Chrome(options=options)
			self._driver.maximize_window()
			self._driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
			self._driver.implicitly_wait(3)
		else:
			self._driver = driver

	def close(self):
		time.sleep(2)
		self._driver.quit()