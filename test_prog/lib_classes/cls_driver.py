from appium import webdriver


class BaseDriver:
    __config: dict

    @classmethod
    def create_driver(cls):
        return webdriver.Remote(command_executor=cls.__config['command_executor'],
                                desired_capabilities=cls.__config['desired_capabilities'])

    @classmethod
    def set_config(cls, config):
        cls.__config = config


if __name__ == '__main__':
    print('тест запускается с body_test.py')
