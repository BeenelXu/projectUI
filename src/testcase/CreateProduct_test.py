import unittest
from time import sleep
from src.common.MyTest import MyTest
from src.function.CreateProductPage import CreateProductPage


class CreateProductTest(MyTest):
    """创建产品测试"""

    # 测试创建客房
    def test_create_room(self):
        CreateProductPage(self.driver).create_room_page()
        sleep(10)
        name = CreateProductPage(self.driver)
        self.assertEqual(name.create_room_success(), "test客房001")

        # 测试创建门票

        # 测试创建票券


if __name__ == "__main__":
    unittest.main()
