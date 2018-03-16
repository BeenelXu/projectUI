from time import sleep
from selenium.webdriver.common.by import By
from src.common import eleaction
from src.common.baseaction import BaseAction

conf = eleaction.EleAction("控件.ini")
data = eleaction.EleAction("数据.ini")


class LoginEntity(BaseAction):
    """用户登录页面"""
    url = "/public/login"
    user_loc = conf.get_eleinfo("登录", "username")
    pwd_loc = conf.get_eleinfo("登录", "password")
    login_loc = conf.get_eleinfo("登录", "login")

    def yunke_login(self):
        self.findelement(*self.user_loc).click()
        sleep(1)
        self.findelement(*self.pwd_loc).click()

    # 输入用户名
    def Input_User(self, username):
        self.findelement(*self.user_loc).send_keys(username)

    # 输入密码

    def Input_Pwd(self, password):
        self.findelement(*self.pwd_loc).send_keys(password)

    # 登录操作
    def click_login(self):
        self.findelement(*self.login_loc).click()

    def user_login(self, username="test1", password="123456!qaz"):
        """
        定义统一登录入口
        :return:
        登录成功
        """
        print("登录浏览器")
        self.open()
        self.yunke_login()
        self.Input_User(username)
        self.Input_Pwd(password)
        sleep(10)
        self.click_login()

    user_login_sucess_loc = (By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/span/span/a')

    def user_login_success(self):
        return self.findelement(*self.user_login_sucess_loc).text


if __name__ == "__main__":
    login1 = LoginEntity()
    login1.user_login()
