# -*- coding: utf-8 -*-
import requests
import unittest
import json


class SearchStu(unittest.TestCase):

    def test_search_stu(self):
        url = "http://api.nnzhp.cn/api/user/stu_info?stu_name=test001"
        res = requests.get(url).json()
        print(res)
        self.assertEqual(res["error_code"], 0)
        self.assertEqual(res["stu_info"][0]['id'], 4058)


if __name__ == "__main__":
    unittest.main()
