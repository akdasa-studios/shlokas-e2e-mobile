class InterfacePrimitive:
    type_obj: str
    key_flag: str
    value_flag: str

    def set_primitive(self, type_obj: str = '', key_flag: str = '', value_flag: str = ''):
        self.type_obj = type_obj
        self.key_flag = key_flag
        self.value_flag = value_flag


if __name__ == '__main__':
    print('тест запускается с body_test.py')
