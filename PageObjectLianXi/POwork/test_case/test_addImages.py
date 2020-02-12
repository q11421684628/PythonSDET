from PageObjectLianXi.POwork.page.managementtool_page import ManagementTool
import os

class TestAddImages:
	def setup(self):
		self.add_images = ManagementTool()

	def test_add_images(self):
		print(os.path.dirname(os.getcwd()))
		path =os.path.abspath(os.path.dirname(os.getcwd())) + r"\upload_image.jpg"
		self.add_images.add_images(path)

	def teardown(self):
		self.add_images.close()