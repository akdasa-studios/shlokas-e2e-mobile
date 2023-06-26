from test_prog.lib_interface_primitives.new_base_primitive import InterfacePrimitive as InPr, By


class WindowLibrary:
    BTN_DWN_BAR_SETTING = InPr(type_obj=By.XPATH, key='test_id', value='settings-tab')
