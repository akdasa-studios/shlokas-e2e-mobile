from test_prog.constants import CURRENT_PATH

desired_capabilities = capabilities = dict(
    platformName='android',
    automationName='uiautomator2',
    deviceName='Pixel_5_API_33',
    appPackage='com.akdasa.shlokas',
    app=f'{CURRENT_PATH}\lib_apps\shlokas-main-54f8d1-debug.apk',
    language='en',
    locale='US'
)

command_executor = '127.0.0.1:4723/wd/hub'

config = {'desired_capabilities': desired_capabilities, 'command_executor': command_executor}


if __name__ == '__main__':
    print('тест запускается с body_test.py')
