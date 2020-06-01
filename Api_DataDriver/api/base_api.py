import json

import requests
import yaml
from jsonpath import jsonpath


class BaseApi:
    params = {}
    data = {}

    @classmethod
    def format(cls, r):
        cls.r = r
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))

    def jsonpath(self, path, r=None, **kwargs):
        if r is None:
            r = self.r.json()
        return jsonpath(r, path)

    # 封装yaml文件的加载
    @classmethod
    def yaml_load(cls, path) -> list:
        with open(path, encoding="UTF-8") as f:
            return yaml.safe_load(f)

    def api_load(self, path):
        return self.yaml_load(path)

    def api_send(self, req: dict):
        req['params']['access_token'] = self.get_token(self.secret)

        # 模板内容替换,使用format替换
        raw = yaml.dump(req)
        for key, value in self.params.items():
            raw = raw.replace(f"${{{key}}}", repr(value))
        req = yaml.safe_load(raw)
        r = requests.request(
            req['method'],
            url=req['url'],
            params=req['params'],
            json=req['json']
        )
        self.format(r)
        return r.json()

    def steps_run(self, steps: list):
        for step in steps:
            print(f"执行到以下步骤:{step}")
            # 将循环出来的值dump下来，然后判断该值在字典params中时就替换掉，
            # 然后在加到yaml文件中
            # 模板内容替换,使用format替换
            raw = yaml.dump(step)
            for key, value in self.params.items():
                raw = raw.replace(f"${{{key}}}", repr(value))
                print(raw)
            step = yaml.safe_load(raw)

            if isinstance(step, dict):
                if "method" in step.keys():
                    method = step['method'].split('.')[-1]
                    print("切割之后为：%s" % method)
                    # 使用getattr函数来完成对切割之后的数据进行加括号调用操作，
                    # 直接调用切割之后的数据加括号调用会报错
                    getattr(self, method)(**step)
                if "extract" in step.keys():
                    self.data['extract'] = getattr(self, "jsonpath")(**step)
                    print(self.data['extract'])
                if "assertion" in step.keys():
                    assertion = step['assertion']
                    if isinstance(assertion, str):
                        assert eval(assertion)
                    if assertion[1] == "eq":
                        assert assertion[0] == assertion[2]