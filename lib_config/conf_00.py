from constants import CURRENT_PATH

desired_capabilities = dict(
    # TODO разобраться с параметрами
    #  (сеанс не вечный. нужно корректное закрытие как со стороны сервера, так и со стороны пользователя)
    platformName='android',
    automationName='uiautomator2',
    deviceName='Pixel_5_API_33',
    appPackage='com.akdasa.shlokas',
    app=f'{CURRENT_PATH}\\lib_apps\\shlokas-main-54f8d1-debug.apk',
    language='en',
    locale='US',
    newCommandTimeout='100'
)

command_executor = '127.0.0.1:4723/wd/hub'

config = {'desired_capabilities': desired_capabilities, 'command_executor': command_executor}
