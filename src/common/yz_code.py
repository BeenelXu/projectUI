import os
from PIL import Image
import pytesseract
from selenium import webdriver
import os


pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract'
tessdata_dir = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
url = 'http://www-test.yunkezan.com/admin/public/login'
driver = webdriver.Chrome(os.path.abspath(r"E:\\chromedriver.exe"))
driver.maximize_window()  # 将浏览器最大化
driver.get(url)
driver.save_screenshot('D:\Tesseract-OCR//aa.png')  # 截取当前网页，该网页有我们需要的验证码
imgelement = driver.find_element_by_xpath('//*[@id="captchaimg"]/img')  # 定位验证码
location = imgelement.location  # 获取验证码x,y轴坐标
size = imgelement.size  # 获取验证码的长宽
rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
          int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
i = Image.open("D:\Tesseract-OCR//aa.png")  # 打开截图
frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
frame4.save('D:\Tesseract-OCR//frame4.jpg')
qq = Image.open('D:\Tesseract-OCR//frame4.jpg')
text = pytesseract.image_to_string(image=qq, lang='eng', config=tessdata_dir).strip()  # 使用image_to_string识别验证码
print(text)
