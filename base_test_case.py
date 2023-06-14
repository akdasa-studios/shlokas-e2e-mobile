import unittest

from anyio import sleep
from class_driver import DriverObj
from lib_config import config_01
from appium.webdriver.common.appiumby import AppiumBy


class BaseTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = DriverObj.create_driver(config_01)
        self.driver.switch_to.context('WEBVIEW_com.akdasa.shlokas')

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def find_by_content(self, query: str):
        selector   = f'//*[contains(text(), "{query}")]'
        elelements = self.driver.find_elements(
            by=AppiumBy.XPATH, value=selector
        )
        return self._get_interactive(elelements)

    def find_by_name(self, query: str):
        selector = f'//*[@name="{query}"]'
        elelements = self.driver.find_elements(
            by=AppiumBy.XPATH, value=selector
        )
        return self._get_interactive(elelements)




    def _get_interactive(self, elements: list):
        interactive_el = None
        for el in elements:
            if el.is_enabled() and el.is_displayed():
                interactive_el = el
        if not interactive_el:
            raise ValueError("Element not found")
        return interactive_el


    # def find(driver, query: str):
    #     if query.startswith("#"):
    #         selector = f'//*[@data-testid="{query[1:]}"]'
    #     if query.startswith("name#"):
    #         selector = f'//*[@name="{query[5:]}"]'
    #     else:
    #         selector = f'//*[contains(text(), "{query}")]'

    #     els = driver.find_elements(by=AppiumBy.XPATH, value=selector)
    #     print(">>> ", els)
    #     interactive_el = None
    #     for el in els:
    #         if el.is_enabled() and el.is_displayed():
    #             interactive_el = el
    #     return interactive_el