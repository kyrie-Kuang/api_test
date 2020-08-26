# -*- coding: utf-8 -*-
import requests
import unittest
import json
from login_base import Login


class GoldAdd(unittest.TestCase):

    def test_gold_add(self):
        login = Login()
        l = login.test_login()
        print(l)

        name = 'niuhanyang='
        c = name + l

        headers = {
            "Cookie": c
        }
        url = "http://api.nnzhp.cn/api/user/gold_add"
        data = {
            "stu_id": 4058,
            "gold": 1000,
        }
        res = requests.post(url=url, data=data, headers=headers).json()
        print(res)
        self.assertEqual(res["error_code"], 0)


if __name__ == "__main__":
    unittest.main()
