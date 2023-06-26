from test_prog.lib_classes.cls_new_test import BaseTest
from test_prog import lib_app_windows as law
from time import sleep


class Test(BaseTest):
    def test_name(self):
        """User should be able to authenticate via email"""
        # Arrange:
        sleep(5)
        description = law.WinStartRegistration.BTN_SIGN_IN_WITH_EMAIL
        email_btn = self.driver.find_obj(description)
        email_btn.click()
        sleep(10)

        # Act:
        description = law.RegistrationByEmail.LABEL_SET_EMAIL
        email_field = self.driver.find_obj(description)
        email_field.click()
        email_field.send_keys('test@shlokas.app')
        sleep(3)

        description = law.RegistrationByEmail.BTN_SEND_EMAIL
        submit = self.driver.find_obj(description)
        submit.click()
        sleep(10)

        # Assert:
        description = law.WindowLibrary.BTN_DWN_BAR_SETTING
        setting = self.driver.find_obj(description)
        setting.click()
        sleep(3)

        description = law.WindowSetting.SLD_ACCOUNT
        account = self.driver.find_obj(description)
        account.click()
        sleep(5)

        description = law.SubWinAccount.TXT_WELCOME
        welcome = self.driver.find_obj(description)
        self.assertTrue(welcome)


if __name__ == '__main__':
    print('тест запускается с body_test.py')
