from Api_DataDriver.api.base_api import BaseApi
from Api_DataDriver.api.wework import WeWork


def api(fun):
    def magic(*args, **kwargs):
        # 首先要让程序知道获取的是哪个类
        base_api: BaseApi = args[0]
        method = fun.__name__
        print(f"当前method的值为：{method}")
        base_api.params = kwargs
        print(f"当前params的值为:{base_api.params}")
        req = base_api.api_load("../api/tag_api.yaml")[method]
        return base_api.api_send(req)

    return magic


class Tag(WeWork):
    secret = "deyWQ65jMKgJfkg6uYabuUBjc879AYY_P-IaP73y7t0"

    def __init__(self):
        self.data = self.api_load("../api/tag_api.yaml")

    def get(self, **kwargs):
        return self.api_send(self.data['get'])

    # def get(self):
    #     url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
    #     r = requests.post(
    #         url,
    #         params={"access_token": self.get_token(self.secret)},
    #         json={"tag_id": []}
    #     )
    #     self.format(r)
    #     return r.json()

    """不使用数据驱动时的写法"""
    # def add(self, name):
    #     url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
    #     r = requests.post(
    #         url,
    #         params={"access_token": self.get_token(self.secret)},
    #         json={
    #             "group_id": "etlFcnCwAAWo2hIOw5E8HLw4I9jiPcfw",
    #             "tag":
    #                 [
    #                     {
    #                         "name": name
    #                     }
    #                 ]
    #         }
    #     )
    #     self.format(r)
    #     return r.json()

    """使用数据驱动时的写法"""

    def add(self, name, **kwargs):
        # todo:使用装饰器来完成参数替换
        self.params['name'] = name
        return self.api_send(self.data['add'])

    def update(self):
        pass

    """不使用数据驱动时的写法"""
    # def delete(self, tag_id=[], group_id=[]):
    #     url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
    #     r = requests.post(
    #         url,
    #         params={"access_token": self.get_token(self.secret)},
    #         json={
    #             "group_id": group_id,
    #             "tag_id": tag_id
    #         }
    #     )
    #     self.format(r)
    #     return r.json()

    """使用数据驱动时的写法"""

    def delete(self, group_id=[], tag_id=[]):
        self.params['tag_id'] = tag_id
        self.params['group_id'] = group_id
        return self.api_send(self.data['delete'])

    @api
    def xxx(self, age):
        pass
