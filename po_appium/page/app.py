import datetime

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from po_appium.page.base_page import BasePage
from po_appium.page.main import Main

class App(BasePage):
	_package = "com.xueqiu.android"
	_activity = ".view.WelcomeActivityAlias"

	def start(self):
		if self._driver is None:
			webviews = {
				"platformName": "android",
				"deviceName": "OPPO-A57",
				"appPackage": self._package,
				"appActivity": self._activity,
				# "noReset": True,
				# "reseKeyboard": True,
				# "unicodeKeyboard": True,
				# "skipServerInstallation": True,
				"chromedriverExecutable": r"E:\PythonSDET\chromedriver\chromedriver_2.20.exe"
				# 当多台设备同时开启时，需要指定某台设备运行的话需要udid参数，否则会一直运行adb devices命令下的第一台设备
				# "udid":"emulator-5554"
			}
			self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", webviews)
			self._driver.implicitly_wait(5)
		else:
			self._driver.start_activity(self._package, self._activity)
			#done:kill app start app
		return self

	def restart(self):
		pass

	def stop(self):
		pass

	def main(self) -> Main:
		#todo:wait main page
		def wait_load(driver):
			datetime.datetime.now()
			source = self._driver.page_source
			if "我的" in source:
				return True
			if "同意" in source:
				return True
			return False
		WebDriverWait(self._driver, 30).until(wait_load)
		return Main(self._driver)