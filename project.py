from selenium import webdriver
from uiautomation_pkg_common_webdriver import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def main():
    # desired_caps = DesiredCapabilities.INTERNETEXPLORER
    # desired_caps['se:ieOptions'] = {}
    # desired_caps['se:ieOptions']['ie.ensureCleanSession'] = True
    # desired_caps['se:ieOptions']['ignoreZoomSetting'] = True
    # desired_caps['se:ieOptions']['enablePersistentHover'] = False
    # desired_caps['se:ieOptions']['nativeEvents'] = True
    # desired_caps['se:ieOptions']['requireWindowFocus'] = True
    # driver = webdriver.Ie(capabilities=desired_caps)
    driver = webdriver.Chrome()
    global app
    global UIType
    app = Device(driver)
    UIType = Type(driver)

    app.driver.get('https://southwire-configurator-test.firebaseapp.com/')

main()

