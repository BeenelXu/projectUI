import os
from selenium import webdriver
from src.common import eleaction
path = os.path.abspath(r"E:\\chromedriver.exe")


def Driver():
    dr = webdriver.Chrome(path)
    return dr


def URL():
    cfg = eleaction.EleAction("控件.ini")
    url = cfg.get_value("url", "baseurl")
    return url

if __name__ == "__main__":
    dr1 = Driver()
    dr1.quit()
