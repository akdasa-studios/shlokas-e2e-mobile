# НОВЫЙ ТЕСТ ===

from time import sleep
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from os import getcwd

CURRENT_PATH = getcwd()
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Pixel 5 API 33',
    appPackage='com.akdasa.shlokas',
    app=f'{CURRENT_PATH}/shlokas-main-54f8d1-debug.apk',
    # chromedriverExecutable= "C:\Files\chromedriver.exe",
    language='en',
    locale='US'
)
print()
appium_server_url = 'http://localhost:4723'


def find(driver, query: str):
    if query.startswith("#"):
        selector = f'//*[@data-testid="{query[1:]}"]'
    if query.startswith("name#"):
        selector = f'//*[@name="{query[5:]}"]'
    else:
        selector = f'//*[contains(text(), "{query}")]'

    els = driver.find_elements(by=AppiumBy.XPATH, value=selector)
    print(">>> ", els)
    interactive_el = None
    for el in els:
        if el.is_enabled() and el.is_displayed():
            interactive_el = el
    return interactive_el


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor=appium_server_url,
            desired_capabilities=capabilities
        )
        self.driver.switch_to.context('WEBVIEW_com.akdasa.shlokas')

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_auth_via_email(self) -> None:
        sign_via_email = find(self.driver, "Email")
        sign_via_email.click()

        email_field = find(self.driver, "name#ion-input-0")
        email_field.click()
        email_field.type("test@shlokas.app")
        sleep(5)


    # def test_auth_via_google(self) -> None:
    #     sign_via_email = find(self.driver, "Google")
    #     sign_via_email.click()


if __name__ == '__main__':
    unittest.main()
