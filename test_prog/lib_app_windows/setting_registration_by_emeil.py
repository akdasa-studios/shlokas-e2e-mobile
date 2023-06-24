from test_prog.lib_interface_primitives.xpath_primitives import ObjByXpath


class RegistrationByEmail:
    LABEL_SET_EMAIL = ObjByXpath(key='name', value='ion-input-0')
    BTN_SEND_EMAIL = ObjByXpath(key='text', value='Sign')
