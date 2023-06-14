from appium import webdriver


class DriverObj:

    @classmethod
    def create_driver(cls, config: dict):
        print("!!!! ", config)
        return webdriver.Remote(command_executor=config['command_executor'],
                                desired_capabilities=config['desired_capabilities'])

    # TODO написать метод корректного завершение теста.
    @classmethod
    def del_driver(cls, driver):
        driver.quit()
