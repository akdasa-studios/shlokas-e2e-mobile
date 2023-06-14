from appium import webdriver


class DriverObj:

    @classmethod
    def create_driver(cls, config: dict):
        try:
            return webdriver.Remote(command_executor=config['command_executor'],
                                    desired_capabilities=config['desired_capabilities'])
        except:
            return None

    # TODO написать метод корректного завершение теста.
    @classmethod
    def del_driver(cls, driver):
        driver.quit()
