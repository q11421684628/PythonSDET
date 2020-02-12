from PageObjectLianXi.POwork.page.managementtool_page import ManagementTool
import os

class TestAddImages:
	def setup(self):
		self.add_images = ManagementTool()

	def test_add_images(self):
		# 返回到上一层级的路径
		path =os.path.abspath(os.path.dirname(os.getcwd())) + r"\upload_image.jpg"
		self.add_images.add_images(path)

	def teardown(self):
		self.add_images.close()