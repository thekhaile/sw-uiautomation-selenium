from selenium import webdriver
from unittest import TestCase
from uiautomation_pkg_common_webdriver import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import sys


class ProjectBase(TestCase):
    def setUp(self):
        # #The following code is needed to run IE in order to clear cache
        # desired_caps = DesiredCapabilities.INTERNETEXPLORER
        # desired_caps['se:ieOptions'] = {}
        # desired_caps['se:ieOptions']['ie.ensureCleanSession'] = True
        # desired_caps['se:ieOptions']['ignoreZoomSetting'] = True
        # desired_caps['se:ieOptions']['enablePersistentHover'] = True
        # desired_caps['se:ieOptions']['nativeEvents'] = True
        # desired_caps['se:ieOptions']['requireWindowFocus'] = True
        # self.driver = webdriver.Ie(capabilities=desired_caps)


        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.app = Device(self.driver)
        self.UIType = Type(self.driver)
        self.verification = Verify()
        self.assertion = Assert()
        self.isMobile = self.app.isMobile()
        self.isChromium = False
        self.isSafari = self.app.isSafari()
        self.driver.maximize_window()

        self.screenshotPath = '../../screenshots/'
        self.app.createScreenshotDir(self.screenshotPath)

    def tearDown(self):
        if self.assertion.didThrowError():
            self.app.saveScreenshot(self.id(), path=self.screenshotPath)
        self.driver.close()
        self.driver.quit()