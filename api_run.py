# -*- coding: utf-8 -*-
import unittest
import HTMLTestRunner
import time

# 接口测试用例目录
all_api_case_list = "E:\\kyl\\api_test\\api_case"

discover = unittest.defaultTestLoader.discover(
    all_api_case_list,
    pattern="case_*.py"
)

# 获取当前时间
now = time.strftime("%Y-%m-%d_%H_%M_%S")

# 定义存放路径
filename = "E:\\kyl\\api_test\\api_report\\" + now + "_result.html"

fn = open(filename, "wb")

# 执行测试套件
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fn,
    title=u"接口测试报告",
    description=u"测试用例执行情况："
)

runner.run(discover)
