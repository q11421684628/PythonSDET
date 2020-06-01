import json

import requests

class WeWork:
	token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
	corpid = "wwb360c29f30344ea2"
	token = dict()
	secret = "GVcTvld3QSEZpOCR_74jR-jkt0-Dg8U_d-cONGElUFQ"
	
	@classmethod
	def get_token(cls, secret=secret):
		if secret is None:
			return cls.token[secret]
		if secret not in cls.token.keys():
			# 避免重复请求，当有相同的token时不用再次发送请求，提高速度
			r = cls.get_access_token(secret)
			# print(json.dumps(r, indent=2))
			cls.token[secret] = r["access_token"]
		return cls.token[secret]
	
	@classmethod
	def get_access_token(cls, secret):
		r = requests.get(
			cls.token_url,
			params={"corpid": cls.corpid, "corpsecret": secret})
		return r.json()
	
	@classmethod
	def format(cls, data):
		print(json.dumps(data.json(), indent=2))