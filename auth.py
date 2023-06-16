from time import sleep
from unittest import main
from base_test_case import BaseTestCase


class TestSignIn(BaseTestCase):
    """Tests for sign in"""

    def test_auth_via_email(self) -> None:
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
    main()
