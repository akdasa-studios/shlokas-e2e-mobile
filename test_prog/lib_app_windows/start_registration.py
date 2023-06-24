from test_prog.lib_interface_primitives.xpath_primitives import ObjByXpath


class WinStartRegistration:
    IMG_LOGO = None
    TXT_WELCOME = None
    BTN_ENTER_AS_A_GUEST = ObjByXpath(key='text', value='Enter')
    BTN_SIGN_IN_WITH_GOOGLE = ObjByXpath(key='text', value='Google')
    BTN_SIGN_IN_WITH_EMAIL = ObjByXpath(key='text', value='Email')
