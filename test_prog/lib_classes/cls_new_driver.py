from appium import webdriver


class BaseDriver(webdriver.Remote):
    __config = None

    def __init__(self):
        super().__init__(command_executor=self.__config['command_executor'],
                         desired_capabilities=self.__config['desired_capabilities'])

    @classmethod
    def set_config(cls, config):
        cls.__config = config

    def find_obj(self, obj):
        objects = self.find_elements(by=obj.type_obj, value=obj.value)
        return self._get_interactive(objects, obj.value)

    @staticmethod
    def _get_interactive(elements: list, key: str):
        print(">>> ", elements)
        interactive_el = None
        for el in elements:
            if el.is_enabled() and el.is_displayed():
                interactive_el = el
        if not interactive_el:
            raise ValueError(f'Element {key} not found')
        return interactive_el


if __name__ == '__main__':
    print('тест запускается с body_test.py')
