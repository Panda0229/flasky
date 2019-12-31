import unittest
from login import app
import json


class LoginTest(unittest.TestCase):
    def setUp(self):
        """在进行测试之前，先被执行"""
        # 设置flask工作在测试模式下,打开测试模式可以报错错误信息
        # app.config["TESTING"] = True
        app.testing = True

        # 创建进行web请求的客户端，由flask提供
        self.client = app.test_client()

    """构造单元测试案例"""
    # 测试的时候定义的函数必须以test开头
    def test_empty_user_name_password(self):
        """测试用户名密码不完整的情况"""
        # 测试用户名，密码都不传
        # 利用client客户端模拟发送web请求
        ret = self.client.post("/login", data={})

        # ret是视图返回的相应对象，data属性是相应体的数据
        resp = ret.data

        # loads将json格式数据转换为字典
        resp = json.loads(resp)

        # 拿到返回值之后进行断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)

        # 测试只传用户名
        # 利用client客户端模拟发送web请求
        ret = self.client.post("/login", data={"user_name": "admin"})

        # ret是视图返回的相应对象，data属性是相应体的数据
        resp = ret.data

        # loads将json格式数据转换为字典
        resp = json.loads(resp)

        # 拿到返回值之后进行断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)

        # 测试只传密码
        # 利用client客户端模拟发送web请求
        ret = self.client.post("/login", data={"password": "admin"})

        # ret是视图返回的相应对象，data属性是相应体的数据
        resp = ret.data

        # loads将json格式数据转换为字典
        resp = json.loads(resp)

        # 拿到返回值之后进行断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)

    def test_wrong_user_name_password(self):
        """测试用户名或密码错误"""
        # 利用client客户端模拟发送web请求
        ret = self.client.post("/login", data={"user_name": "itcast", "password": "admin"})

        # ret是视图返回的相应对象，data属性是相应体的数据
        resp = ret.data

        # loads将json格式数据转换为字典
        resp = json.loads(resp)

        # 拿到返回值之后进行断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 2)


if __name__ == '__main__':
    unittest.main()
