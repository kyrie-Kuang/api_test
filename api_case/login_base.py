# -*- coding: utf-8 -*-
import requests
import unittest
import json


class Login():
    def test_login(self):
        url = "http://api.nnzhp.cn/api/user/login"
        data = {
            'username': 'niuhanyang',
            'passwd': 'aA123456'
        }
        res = requests.post(url=url, data=data)
        t = res.text
        # print(t)
        # 将响应内容转换为Json对象
        json_obj = json.loads(t)
        # print(json_obj)
        # 从Json对象获取想要内容
        cookie = json_obj['login_info']['sign']
        return cookie


if __name__ == "__main__":
    unittest.main()
