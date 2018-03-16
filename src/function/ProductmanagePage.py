from src.common import eleaction
from src.common.baseaction import BaseAction

conf = eleaction.EleAction("控件.ini")
data = eleaction.EleAction("数据.ini")


class ProductmanagePageEntity(BaseAction):
    """产品管理页面"""
    url = "/roomstyle/index"
    productmanage_loc = conf.get_eleinfo("列表", "产品管理")
    productlist_loc = conf.get_eleinfo("产品管理", "产品列表")
    room_loc = conf.get_eleinfo("产品管理", "客房列表")
    ticket_loc = conf.get_eleinfo("产品管理", "门票列表")
    creatproduct_loc = conf.get_eleinfo("产品管理", "创建产品")
    select_hotel_loc = conf.get_eleinfo("产品管理", "选择商家")
    hotel_loc = conf.get_eleinfo("选择商家", "商家")
    room_type_loc = conf.get_eleinfo("选择商家", "客房")
    menticket_type_loc = conf.get_eleinfo("选择商家", "门票")
    ticket_type_loc = conf.get_eleinfo("选择商家", "票券")
    direct_selling_doc = conf.get_eleinfo("选择商家", "直销")
    direct_purchase_doc = conf.get_eleinfo("选择商家", "直采")
    submit_click_doc = conf.get_eleinfo("选择商家", "确认")

    # 点击创建产品
    def click_create_product(self):
        self.findelement(*self.creatproduct_loc).click()

    # 选择归属商家
    def owner_hotel(self):
        self.select(*self.select_hotel_loc, *self.hotel_loc)

    # 选择客房商品类型
    def owner_room(self):
        self.findelement(*self.room_type_loc).click()

    # 选择门票商品类型
    def owner_menticket(self):
        self.findelement(*self.menticket_type_loc).click()

    # 选择票券商品类型
    def owner_ticket(self):
        self.findelement(*self.ticket_type_loc).click()

    # 选择直销产品类型
    def owner_direct_selling(self):
        self.findelement(*self.direct_selling_doc).click()

    # 选择直采产品类型
    def owner_direct_purchase(self):
        self.findelement(*self.direct_purchase_doc).click()

    # 确认创建操作
    def submit_click(self):
        self.findelement(*self.submit_click_doc).click()

    def create_room_product(self):
        """
        定义创建客房直销产品
        :return:
        """
        self.click_create_product()
        self.owner_hotel()
        self.owner_room()
        self.owner_direct_selling()
        self.submit_click()

    def creat_menticket_product(self):
        """
        定义创建门票直销产品
        :return:
        """
        self.click_create_product()
        self.owner_hotel()
        self.owner_menticket()
        self.owner_direct_selling()
        self.submit_click()

    def creat_ticket_product(self):
        """
        定义创建票券直销产品
        :return:
        """
        self.click_create_product()
        self.owner_hotel()
        self.owner_ticket()
        self.owner_direct_selling()
        self.submit_click()


