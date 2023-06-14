from constants import CURRENT_PATH

desired_capabilities = capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Pixel 5 API 33',
    appPackage='com.akdasa.shlokas',
    app=f'{CURRENT_PATH}/shlokas-main-54f8d1-debug.apk',
    language='en',
    locale='US'
)

command_executor = 'http://localhost:4723'

config = {'desired_capabilities': desired_capabilities, 'command_executor': command_executor}
