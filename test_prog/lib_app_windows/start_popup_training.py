from test_prog.lib_interface_primitives.new_base_primitive import InterfacePrimitive as InPr, By


class PopUpTraining:
    INFO_LABEL = None
    BTN_YES = InPr(type_obj=By.XPATH, key='text', value='Yes')
    BTN_NO = InPr(type_obj=By.XPATH, key='text', value='No')

    TEXT_FIRST_STEP = None
    SLOKA_G_1_1 = InPr(type_obj=By.XPATH, key='text', value='BG 1.1')

