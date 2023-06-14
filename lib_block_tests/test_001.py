from appium.webdriver.common.appiumby import By

name_test = 'test_001'


def test(driver):

    button = 'start'
    while button != 'exit_test':
        button = input('> ')
        if button != 'exit_test':
            try:
                driver.find_element(by=By.XPATH, value=f'//*[@text="{button}"]').click()
            except Exception as e:
                print("No interactive elements")
                print(e)


block_test = {'name_test': name_test, 'link_test': test}
