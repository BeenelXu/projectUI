from time import sleep
from selenium.webdriver.common.by import By
from src.common import eleaction
from src.common.baseaction import BaseAction
from src.function.LoginPage import LoginEntity

conf = eleaction.EleAction("控件.ini")
data = eleaction.EleAction("数据.ini")


class CreateProductPage(BaseAction):
    """创建产品页面"""
    url = "/roomstyle/roomStyleAE?cateId=1&theHotelId=227"
    pic_file = "C:\\Users\\xuyuan\\Desktop\\testpic.jpg"
    roomName_loc = conf.get_eleinfo("创建客房", "房型名称")
    roomName_value = data.get_eleinfo("创建客房", "房型名称")
    roomStyleAlias_loc = conf.get_eleinfo("创建客房", "房型别名")
    roomStyleAlias_value = data.get_eleinfo("创建客房", "房型别名")
    area_loc = conf.get_eleinfo("创建客房", "房间面积")
    area_value = data.get_eleinfo("创建客房", "房间面积")
    bedType_loc = conf.get_eleinfo("创建客房", "床型")
    bedType_value = data.get_eleinfo("创建客房", "床型")
    bedSize_loc = conf.get_eleinfo("创建客房", "床型尺寸")
    bedSize_value = data.get_eleinfo("创建客房", "床型尺寸")
    floor_loc = conf.get_eleinfo("创建客房", "楼层")
    floor_value = data.get_eleinfo("创建客房", "楼层")
    maxOccupancy_loc = conf.get_eleinfo("创建客房", "可住人数")
    maxOccupancy_value = data.get_eleinfo("创建客房", "可住人数")
    addPicture_loc = conf.get_eleinfo("创建客房", "添加图片")
    submit_create_click_loc = conf.get_eleinfo("创建客房", "确认")
    cancel_create_click_loc = conf.get_eleinfo("创建客房", "取消")

    # 输入房型名称
    def input_room_name(self):
        self.findelement(*self.roomName_loc).send_keys(*self.roomName_value)

    # 输入房型别名
    def input_room_style_alias(self):
        self.findelement(*self.roomStyleAlias_loc).send_keys(*self.roomStyleAlias_value)

    # 输入房间面积
    def input_area(self):
        self.findelement(*self.area_loc).send_keys(*self.area_value)

    # 输入床型
    def input_bed_type(self):
        self.findelement(*self.bedType_loc).send_keys(*self.bedType_value)

    # 输入床型尺寸
    def input_bed_size(self):
        self.findelement(*self.bedSize_loc).send_keys(*self.bedSize_value)

    # 输入楼层
    def input_floor(self):
        self.findelement(*self.floor_loc).send_keys(*self.floor_value)

    # 输入可住人数
    def input_max_occupancy(self):
        self.findelement(*self.maxOccupancy_loc).send_keys(*self.maxOccupancy_value)

    # 添加产品图片
    def add_picture(self):
        self.driver.get(self.pic_file)
        self.findelement(*self.addPicture_loc).send_keys(self.pic_file)

    # 确认创建
    def submit_create_click(self):
        self.findelement(*self.submit_create_click_loc).click()

    # 取消创建
    def cancel_create_click(self):
        self.findelement(*self.cancel_create_click_loc).click()

    def create_room_page(self):
        """
        创建客房产品页面
        :return:
        """
        LoginEntity(self.driver).user_login()
        self.open()
        current_url = self.driver.current_url
        print(current_url)
        self.input_room_name()
        self.input_room_style_alias()
        self.input_area()
        self.input_bed_type()
        self.input_bed_size()
        self.input_floor()
        self.input_max_occupancy()
        sleep(10)
        self.add_picture()
        sleep(10)
        self.submit_create_click()
        sleep(10)
        self.submit_create_click()

    room_create_success_loc = (By.XPATH, '//*[@id="j-orderlist"]/tbody/tr[1]/td[3]')

    # 定义创建客房成功
    def create_room_success(self):
        return self.findelement(*self.room_create_success_loc).text
