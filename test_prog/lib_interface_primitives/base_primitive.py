from appium.webdriver.common.appiumby import By


class InterfacePrimitive:
    key_str = None

    @staticmethod
    def _get_interactive(elements: list, key: str):
        print(">>> ", elements)
        interactive_el = None
        for el in elements:
            if el.is_enabled() and el.is_displayed():
                interactive_el = el
        if not interactive_el:
            raise ValueError(f'Element {key} not found')
        return interactive_el


if __name__ == '__main__':
    print('тест запускается с body_test.py')
