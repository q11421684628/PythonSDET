import json

from APITest.test_wework.api.groupchat import GroupChat
from APITest.test_wework.api.wework import WeWork

class TestWeWork:
    secret = "EQrjhPeM7ghjx3-FVFMiY5UpW5t-CyJ-7FyH8e_oSQA"
    # secret = "deyWQ65jMKgJfkg6uYabuUBjc879AYY_P-IaP73y7t0"
    @classmethod
    def setup_class(cls):
        cls.groupchat = GroupChat()

    def test_groupchat_get(self):
        r = self.groupchat.list()
        assert r["errcode"] == 0

    def test_groupchat_get_status(self):
        r = self.groupchat.list(status_filter=1)
        print(json.dumps(r, indent=2))
        assert r["errcode"] == 0

    def test_groupchat_detail(self):
        r = self.groupchat.list()
        chat_id = r["group_chat_list"][0]["chat_id"]
        r = self.groupchat.get(chat_id)
        assert r["errcode"] == 0
