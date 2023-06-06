import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Pixel_3a_API_33_x86_64',
    appPackage='com.akdasa.shlokas',
    # appActivity='.Settings',
    app=r'C:\\Users\Smith\PycharmProjects\test_appi\shlokas-main-54f8d1-debug.apk',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(command_executor=appium_server_url, desired_capabilities=capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:

        button = input('Введите проверяемую кнопку: ')
        while button:
            try:
                self.driver.find_element(by=AppiumBy.XPATH, value=f'//*[@text="{button}"]').click()
            except:
                print('Такой кнопки нет.')
            button = input('Введите проверяемую кнопку: ')


if __name__ == '__main__':
    unittest.main()
