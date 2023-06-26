from appium.webdriver.common.appiumby import By


class InterfacePrimitive:
    def __init__(self, type_obj: By, key: str = '', value: str = ''):
        self.type_obj = type_obj
        if type_obj == By.XPATH and key != '':
            self.create_key_str(key, value)
        else:
            self.value = value

    def create_key_str(self, key, value):
        if key == 'text':
            self.value = f'//*[contains(text(), "{value}")]'
        elif key == 'name':
            self.value = f'//*[@name="{value}"]'
        elif key == 'test_id':
            self.value = f'//*[@data-testid="{value}"]'


if __name__ == '__main__':
    print('тест запускается с body_test.py')
