import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from os import getcwd
from json import dumps

CURRENT_PATH = getcwd()


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Pixel 5 API 33',
    appPackage='com.akdasa.shlokas',
    app=f'{CURRENT_PATH}/shlokas-main-54f8d1-debug.apk',
    language='en',
    locale='US'
)
appium_server_url = 'http://localhost:4723'


driver = webdriver.Remote(
    command_executor=appium_server_url,
    desired_capabilities=capabilities
)
driver.switch_to.context('WEBVIEW_com.akdasa.shlokas')
print(driver.contexts)
print(dumps(capabilities))



button = "inital"
while button:
    button = input('> ')

    if button.startswith("#"):
        selector = f'//*[@data-testid="{button[1:]}"]'
    else:
        selector = f'//*[contains(text(), "{button}")]'
    print(selector)

    try:
        els = driver.find_elements(by=AppiumBy.XPATH, value=selector)
        interactive_el = None
        for el in els:
            if el.is_enabled() and el.is_displayed():
                interactive_el = el
        if interactive_el:
            print(interactive_el.text)
            interactive_el.click()
        else:
            print("No interactive elements")
    except Exception as e:
        print(e)

#inbox-tab-badge
driver.quit()
