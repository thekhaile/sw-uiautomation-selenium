from selenium import webdriver
from unittest import TestCase
from common import *


class ProjectBase(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.app = Device(self.driver)
        self.UIType = Type(self.driver)
        self.verification = Verify()
        self.assertion = Assert()
        self.isMobile = self.app.isMobile()
        self.isChromium = False
        if self.driver.current_context == 'CHROMIUM':
            self.isChromium = True

    def tearDown(self):
        self.driver.quit()