from selenium.webdriver.support.wait import WebDriverWait

yunke_url = "http://www-test.yunkezan.com/admin"


class BaseAction(object):
    """对元素操作的公共方法进行封装，并增加日志记录处理"""
    def __init__(self, driver, base_url=yunke_url, parent=None):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' %url

    def findelement(self, *loc):
        return self.driver.find_element(*loc)

    def findelements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, src):
        return self.driver.execute_script(src)

    def isexist(self, *loc):
        """判断元素是否存在"""
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_elements(*loc))
            Exist = True
        except TimeoutError:
            Exist = False
            print("查找元素超时")
        return Exist

    def click(self, *loc):
        """click操作"""
        ele = self.findelement(*loc)
        ele.click()

    def sendkeys(self, *loc, value):
        """send_keys操作"""
        ele = self.findelement(*loc)
        ele.clear
        ele.send_keys(value)



