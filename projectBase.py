from selenium import webdriver
from unittest import TestCase
from uiautomation_pkg_common_webdriver import *


class ProjectBase(TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(5)
        self.app = Device(self.driver)
        self.UIType = Type(self.driver)
        self.verification = Verify()
        self.assertion = Assert()
        self.isMobile = self.app.isMobile()
        self.isChromium = False
        self.isSafari = self.app.isSafari()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()