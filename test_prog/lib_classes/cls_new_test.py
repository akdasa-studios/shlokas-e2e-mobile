import unittest
from test_prog.lib_classes.cls_new_driver import BaseDriver


class BaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = BaseDriver()
        self.driver.switch_to.context('WEBVIEW_com.akdasa.shlokas')

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def get_driver(self):
        return self.driver


if __name__ == '__main__':
    print('тест запускается с body_test.py')
