from test_prog.lib_interface_primitives.new_base_primitive import InterfacePrimitive as InPr, By


class RegistrationByEmail:
    LABEL_SET_EMAIL = InPr(type_obj=By.XPATH, key='name', value='ion-input-0')
    BTN_SEND_EMAIL = InPr(type_obj=By.XPATH, key='text', value='Sign')
