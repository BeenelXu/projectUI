import unittest
from src.common.launchdriver import Driver


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    #def tearDown(self):
        #self.driver.quit()
