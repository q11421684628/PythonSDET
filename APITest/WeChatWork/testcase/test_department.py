from APITest.WeChatWork.Api.DepartmentApi import Department

class TestDepartment:
	
	@classmethod
	def setup_class(cls):
		cls.department = Department()
	
	def test_create_department(self):
		create_source = self.department.create_department("部门2", "1")
		assert create_source["errmsg"] == "created"
	
	def test_get_department(self):
		get_department = self.department.get_department()
		assert get_department["errmsg"] == "ok"
	
	def test_update_department(self):
		create_department = self.department.create_department("部门3", "1")
		self.department_id = create_department["id"]
		update_department = self.department.update_department(self.department_id, name="部门9")
		assert update_department["errmsg"] == "updated"
	
	def test_delete_department(self):
		create_department = self.department.create_department("部门5", "1")
		self.id = create_department["id"]
		delete_department = self.department.delete_department(self.id)
		assert delete_department["errmsg"] == "deleted"