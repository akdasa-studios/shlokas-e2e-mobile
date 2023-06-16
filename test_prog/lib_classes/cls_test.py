from test_prog.lib_classes.cls_test_methods import TestMethods
from test_prog.lib_classes.cls_driver import BaseDriver


class BaseTest(TestMethods):
    def setUp(self) -> None:
        self.driver = BaseDriver.create_driver()
        self.driver.switch_to.context('WEBVIEW_com.akdasa.shlokas')

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()


if __name__ == '__main__':
    print('тест запускается с body_test.py')
