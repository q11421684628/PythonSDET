import json

import requests

from APITest.WeChatWork.Api.wework import WeWork

class Department(WeWork):
	department_id = None
	
	def create_department(self, name, parentid, **kwargs):
		json_data = {"name": name, "parentid": parentid}
		json_data.update(kwargs)
		create_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
		r = requests.post(
			create_url,
			params={"access_token": self.get_token(self.secret)},
			json=json_data
		)
		# print(json.dumps(r.json(), indent=2))
		return r.json()
	
	def get_department(self, **kwargs):
		params = {"access_token": self.get_token(self.secret)}
		params.update(kwargs)
		get_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
		r = requests.get(
			get_url,
			params= params
		)
		return r.json()
	
	def update_department(self, id, **kwargs):
		json_data={"id": id}
		json_data.update(kwargs)
		update_url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
		r = requests.post(
			update_url,
			params={"access_token": self.get_token(self.secret)},
			json=json_data
		)
		# print(json.dumps(r.json(), indent=2))
		return r.json()
	
	def delete_department(self, id):
		delete_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
		r = requests.get(
			delete_url,
			params={"access_token": self.get_token(self.secret), "id":id}
		)
		print(json.dumps(r.json(), indent=2))
		return r.json()
	