import unittest
from time import sleep
from src.common.MyTest import MyTest
from src.function.LoginPage import LoginEntity


class LoginTest(MyTest):
    """云客登录测试"""

    # 测试用户登录
    def user_login_verify(self, username="", password=""):
        LoginEntity(self.driver).user_login(username, password)

    def test_login1(self):
        """用户名、密码正确"""
        self.user_login_verify(username="test1", password="123456!qaz")
        sleep(10)
        po = LoginEntity(self.driver)
        self.assertEqual(po.user_login_success(), "test1")


if __name__ == "__main__":
    unittest.main()
