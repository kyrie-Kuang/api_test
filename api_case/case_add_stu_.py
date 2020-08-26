# -*- coding: utf-8 -*-
import requests
import unittest
import json


class AddStu(unittest.TestCase):

    def test_add_stu(self):
        url = "http://api.nnzhp.cn/api/user/add_stu"
        data = {
            "name": "micr067",
            "grade": "白羊座",
            "phone": 18180470005,
            "sex": "男",
            "age": 26,
            "addr": "北京市朝阳区"
        }
        res = requests.post(url=url, data=json.dumps(data)).json()
        print(res)
        self.assertEqual(res["error_code"], 0)
        self.assertEqual(res["msg"], "操作成功！")


if __name__ == "__main__":
    unittest.main()
