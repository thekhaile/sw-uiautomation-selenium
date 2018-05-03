from selenium import webdriver
from unittest import TestCase
from uiautomation_pkg_common_webdriver import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

class ProjectBase(TestCase):
    def setUp(self):
        user = 'mmqaautomation@gmail.com'
        key = '/SGHPosrUb.eHKU2QIZE-7nA1yd8O2c9sGIGRvKqo'
        version = 'placeholderVersion'
        runId = 'placeholderRunId'
        self.caseId = ''
        self.client = APIClient(runId=runId, version=version, user=user, key=key)
        # """The following code is needed to run IE in order to clear cache"""
        # desired_caps = DesiredCapabilities.INTERNETEXPLORER
        # desired_caps['se:ieOptions'] = {}
        # desired_caps['se:ieOptions']['ie.ensureCleanSession'] = True
        # desired_caps['se:ieOptions']['ignoreZoomSetting'] = True
        # desired_caps['se:ieOptions']['enablePersistentHover'] = True
        # desired_caps['se:ieOptions']['nativeEvents'] = True
        # desired_caps['se:ieOptions']['requireWindowFocus'] = True
        # self.driver = webdriver.Ie(capabilities=desired_caps)
        # """End of IE block"""

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.app = Device(self.driver)
        self.UIType = Type(self.driver)
        self.verification = Verify()
        self.assertion = Assert()
        self.isMobile = self.app.isMobile()
        self.isChromium = False
        self.isSafari = self.app.isSafari()
        self.isInternetExplorer = self.app.isInternetExplorer()
        self.isFirefox = self.app.isFirefox()
        self.driver.maximize_window()

        self.screenshotPath = '../../screenshots/'
        self.app.createScreenshotDir(self.screenshotPath)

    def tearDown(self):
        if self.assertion.didThrowError():
            resultFlag = False
            try:
                self.app.saveScreenshot(self.id(), path=self.screenshotPath)
            except:
                pass
        else:
            resultFlag = True
        try:
            self.client.updateTestrail(self.caseId, resultFlag)
        except:
            pass
        finally:
            if self.isInternetExplorer():
                """Make sure that all IE instances are closed since each run opens 2 IE instances"""
                os.system('TASKKILL /F /IM iexplore.exe /T')

            elif self.isSafari and self.assertion.didThrowError():
                """Make sure that Safari Automated Session is killed before starting a new one"""
                try:
                    os.system('kill $(ps aux | grep "Safari --automation" | awk "{print $2}")')
                except:
                    pass
            else:
                self.driver.close()
            if not (self.isFirefox() or self.isSafari()):
                self.driver.quit()
