from test_prog.lib_classes.cls_test import BaseTest
from time import sleep


class Test(BaseTest):
    def test_name(self):
        """User should be able to authenticate via email"""
        # Arrange:
        email_btn = self.find_by_content("Email")
        email_btn.click()

        # Act:
        email_field = self.find_by_name("ion-input-0")
        email_field.click()
        email_field.send_keys("test@shlokas.app")

        submit = self.find_by_content("Sign")
        submit.click()
        sleep(5)

        # Assert:
        self.find_by_test_id("settings-tab").click()
        self.find_by_content("Account").click()

        self.assertTrue(
            self.find_by_content("Welcome")
        )


if __name__ == '__main__':
    print('тест запускается с body_test.py')
