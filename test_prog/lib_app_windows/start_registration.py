from test_prog.lib_interface_primitives.new_base_primitive import InterfacePrimitive as InPr, By


class WinStartRegistration:
    IMG_LOGO = None
    TXT_WELCOME = None
    BTN_ENTER_AS_A_GUEST = InPr(type_obj=By.XPATH, key='text', value='Enter')
    BTN_SIGN_IN_WITH_GOOGLE = InPr(type_obj=By.XPATH, key='text', value='Google')
    BTN_SIGN_IN_WITH_EMAIL = InPr(type_obj=By.XPATH, key='text', value='Email')
