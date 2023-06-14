from class_driver import DriverObj

from appium.webdriver.common.appiumby import By


class TestObj:
    def __init__(self, tests: dict):
        self.critical_error = False
        # TODO написать метод запуска приложений для теста (appium, эмулятор).
        # TODO driver: имеет место различное поведение при различных ошибках конфигурации (нужно как-то их обработать)
        self.driver, self.critical_error = (DriverObj.create_driver(tests['conf']), False) if not self.critical_error else (None, True)
        self.list_test, self.critical_error = (tests['list_test'], False) if not self.critical_error else (None, True)

    def check_create_test_obj(self):
        return True if not self.critical_error else False

    def run_test(self):
        for test in self.list_test:
            try:
                test['link_test'](self.driver)
                print(f"{test['name_test']}  - OK\n")
            except:
                print(f"{test['name_test']}   - NO\n")

    def run_manual_test(self):
        button = 'start'
        while button != 'exit_test':
            button = input('> ')
            if button != 'exit_test':
                try:
                    self.driver.find_element(by=By.XPATH, value=f'//*[@text="{button}"]').click()
                except Exception as e:
                    print("No interactive elements")
                    print(e)
