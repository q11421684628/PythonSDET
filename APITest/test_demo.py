import json

import requests


def test_requests():
    r = requests.get('https://home.testing-studio.com/categories.json')
    print(r.status_code)
    print(r.json())
    assert r.status_code == 200


def test_get():
    r = requests.get("https://httpbin.testing-studio.com/get",
                     params={
                         "a": 1,
                         "b": 2,
                         "c": "ccc"
                     })
    print(r.json())
    assert r.status_code == 200


def test_post():
    r = requests.post("https://httpbin.testing-studio.com/post",
                      params={
                          "a": 1,
                          "b": 2,
                          "c": "ccc"
                      },
                      data={
                          "a": 11,
                          "b": 22,
                          "c": "cccccc"
                      },
                      headers={"h": "header demo"}
                      )
    print(r.json())
    assert r.status_code == 200
    assert r.json()["headers"]["H"] == "header demo"


def test_upload():
    r = requests.post("https://httpbin.testing-studio.com/post", files=dict(
        file=open("E:\PythonSDET\APITest\__init__.py", "rb")),
        cookies={"name": "xiaoxi"}
    )
    print(r.json())
    assert r.status_code == 200


def test_get_hooks():
    def modify_response(r, *args, **kwargs):
        r.demo = "demo content"
        return r
    r = requests.get("https://httpbin.testing-studio.com/get",
                     params={
                         "a": 1,
                         "b": 2,
                         "c": "ccc"
                     },
                     hooks={"response": [modify_response]}
                     )
    print(json.dumps(r.json(), indent=2))
    print(r.demo)
    assert r.status_code == 200
