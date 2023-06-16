import unittest
from appium.webdriver.common.appiumby import By


class TestMethods(unittest.TestCase):
    driver = None

    def find_by_content(self, query: str):
        selector = f'//*[contains(text(), "{query}")]'
        elelements = self.driver.find_elements(
            by=By.XPATH, value=selector
        )
        return self._get_interactive(elelements)

    def find_by_name(self, query: str):
        selector = f'//*[@name="{query}"]'
        elelements = self.driver.find_elements(
            by=By.XPATH, value=selector
        )
        return self._get_interactive(elelements)

    def find_by_test_id(self, query: str):
        selector = f'//*[@data-testid="{query}"]'
        elelements = self.driver.find_elements(
            by=By.XPATH, value=selector
        )
        return self._get_interactive(elelements)

    @staticmethod
    def _get_interactive(elements: list):
        print(">>> ", elements)
        interactive_el = None
        for el in elements:
            if el.is_enabled() and el.is_displayed():
                interactive_el = el
        if not interactive_el:
            raise ValueError("Element not found")
        return interactive_el
