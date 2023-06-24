from test_prog.lib_interface_primitives.base_primitive import InterfacePrimitive, By


class ObjByXpath(InterfacePrimitive):

    def __init__(self, key: str, value: str):
        super().__init__()
        self.key = key
        self.value = value
        self.create_key_str()

    def create_key_str(self):
        if self.key == 'text':
            self.key_str = f'//*[contains(text(), "{self.value}")]'
        elif self.key == 'name':
            self.key_str = f'//*[@name="{self.value}"]'
        elif self.key == 'test_id':
            self.key_str = f'//*[@data-testid="{self.value}"]'

    def find_obj(self, driver):
        objects = driver.find_elements(by=By.XPATH, value=self.key_str)
        return self._get_interactive(objects, self.key_str)
