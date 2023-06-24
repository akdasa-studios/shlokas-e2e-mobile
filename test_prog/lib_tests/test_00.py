from test_prog.lib_classes.cls_test import BaseTest
from test_prog import lib_app_windows as law
from time import sleep


class Test(BaseTest):
    def test_name(self):
        """User should be able to authenticate via email"""
        # Arrange:
        sleep(5)
        description = law.WinStartRegistration.BTN_SIGN_IN_WITH_EMAIL
        email_btn = description.find_obj(self.driver)
        email_btn.click()
        sleep(3)

        # Act:
        description = law.RegistrationByEmail.LABEL_SET_EMAIL
        email_field = description.find_obj(self.driver)
        email_field.click()
        email_field.send_keys('test@shlokas.app')
        sleep(3)

        description = law.RegistrationByEmail.BTN_SEND_EMAIL
        submit = description.find_obj(self.driver)
        submit.click()
        sleep(10)

        # Assert:
        description = law.WindowLibrary.BTN_DWN_BAR_SETTING
        setting = description.find_obj(self.driver)
        setting.click()
        sleep(3)

        description = law.WindowSetting.SLD_ACCOUNT
        account = description.find_obj(self.driver)
        account.click()
        sleep(5)

        description = law.SubMenuAccount.TXT_WELCOME
        welcome = description.find_obj(self.driver)
        self.assertTrue(welcome)


if __name__ == '__main__':
    print('тест запускается с body_test.py')
