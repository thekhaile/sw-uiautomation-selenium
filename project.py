from selenium import webdriver
from uiautomation_pkg_common_webdriver import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from southwire_pkg_uiautomation_webdriver.components import *

class Flow():
    def launch(self):
        # #The following code is needed to run IE in order to clear cache
        # desired_caps = DesiredCapabilities.INTERNETEXPLORER
        # desired_caps['se:ieOptions'] = {}
        # desired_caps['se:ieOptions']['ie.ensureCleanSession'] = True
        # desired_caps['se:ieOptions']['ignoreZoomSetting'] = True
        # desired_caps['se:ieOptions']['enablePersistentHover'] = True
        # desired_caps['se:ieOptions']['nativeEvents'] = True
        # desired_caps['se:ieOptions']['requireWindowFocus'] = True
        # self.driver = webdriver.Ie(capabilities=desired_caps)

        # Initializing the driver object and other common objects
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

        # Initializing the objects specific to the project
        self.feederSchedule = FeederSchedule(self)
        self.reelList = ReelList(self)
        self.jobSummary = JobSummary(self)
        self.authentication = Authentication(self)
        self.circuit = Circuit(self)
        self.footer = Footer(self)
        self.job = Job(self)
        self.jobList = JobList(self)
        self.navigation = Navigation(self)
        self.passwordReset = PasswordReset(self)
        self.project = Project(self)
        self.projectList = ProjectList(self)
        self.reel = Reel(self)
        self.registration = Registration(self)

    def quit(self):
        self.driver.close()

def main():
    global flow
    flow = Flow()
    flow.launch()

main()

