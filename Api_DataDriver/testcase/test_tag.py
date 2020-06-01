import pytest

from Api_DataDriver.api.base_api import BaseApi
from Api_DataDriver.api.tag import Tag


class TestTag:
    data = BaseApi.yaml_load("test_tag.data.yaml")

    @classmethod
    def setup_class(cls):
        cls.tag = Tag()
        # cls.data = cls.tag.yaml_load("test_tag.data.yaml")

    def test_get(self):
        r = self.tag.get()
        assert r['errcode'] == 0
        print(self.tag.jsonpath("$..tag[?(@.name=='demo_1')]")[0]["id"])
        print(self.tag.jsonpath(f"$..tag[?(@.name=='demo_1')]"))

    def test_add(self):
        r = self.tag.add("demo_1")
        assert r["errcode"] == 0

    # @pytest.mark.parametrize("name", [
    #     "demo_1", "demo_2", "中文测试", "中文_1", "123", " ", "*", "😀"
    # ])
    @pytest.mark.parametrize("name", data["teast_delete"])
    def test_delete(self, name):
        # 如果有就删除
        r = self.tag.get()
        x = self.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")
        if isinstance(x, list) and len(x) > 0:
            self.tag.delete(tag_id=[x[0]["id"]])

        # 环境干净之后再开始测试
        r = self.tag.get()
        path = "$..tag[?(@.name!=  '')]"
        size = len(self.tag.jsonpath(path))
        # 添加新标签
        self.tag.add(name)
        r = self.tag.get()
        assert len(self.tag.jsonpath(path)) == size+1
        tag_id = self.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")[0]["id"]
        # 删除新标签
        self.tag.delete(tag_id=[tag_id])
        # 断言
        r = self.tag.get()
        assert len(self.tag.jsonpath(path)) == size