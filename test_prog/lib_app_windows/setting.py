from test_prog.lib_interface_primitives.new_base_primitive import InterfacePrimitive as InPr, By


class WindowSetting:
    SLD_ACCOUNT = InPr(type_obj=By.XPATH, key='text', value='Account')


class SubWinAccount:
    TXT_WELCOME = InPr(type_obj=By.XPATH, key='text', value='Welcome')
