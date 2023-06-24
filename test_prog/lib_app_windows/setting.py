from test_prog.lib_interface_primitives.xpath_primitives import ObjByXpath


class WindowSetting:
    SLD_ACCOUNT = ObjByXpath(key='text', value='Account')


class SubMenuAccount:
    TXT_WELCOME = ObjByXpath(key='text', value='Welcome')
