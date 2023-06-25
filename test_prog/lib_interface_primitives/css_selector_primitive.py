from test_prog.lib_interface_primitives.base_primitive import InterfacePrimitive, By


class ObjByCssSelector(InterfacePrimitive):

    def __init__(self, value: str):
        super().__init__()
        self.value = value

    def find_obj(self, driver):
        objects = driver.find_elements(by=By.CSS_SELECTOR, value=self.value)
        return self._get_interactive(objects, self.value)
