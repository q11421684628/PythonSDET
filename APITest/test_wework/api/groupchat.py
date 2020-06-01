import json

import requests

from APITest.test_wework.api.wework import WeWork

class GroupChat(WeWork):
	secret = "deyWQ65jMKgJfkg6uYabuUBjc879AYY_P-IaP73y7t0"
	
	def list(self,offset=0, limit=1000,  **kwargs):
		json={"offset": offset, "limit": limit}
		json.update(**kwargs)
		url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list"
		r = requests.post(
			url,
			params={"access_token": self.get_token(self.secret)},
			json=json
		)
		return r.json()
	
	def get(self, chat_id):
		detail_url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get"
		r = requests.post(
			detail_url,
			params={"access_token": self.get_token(self.secret)},
			json={"chat_id": chat_id}
		)
		print(json.dumps(r.json(), indent=2))
		return r.json()