from test_prog.lib_classes.cls_new_test import BaseTest
from test_prog import lib_app_windows as law
from time import sleep


class Test(BaseTest):
    def test_name(self):
        # Arrange:
        sleep(2)
        description = law.WinStartRegistration.BTN_ENTER_AS_A_GUEST
        email_btn = self.driver.find_obj(description)
        email_btn.click()
        sleep(2)

        description = law.PopUpTraining.BTN_YES
        no_btn = self.driver.find_obj(description)
        no_btn.click()
        sleep(15)

        description = law.PopUpTraining.SLOKA_G_1_1
        g_1_1 = self.driver.find_obj(description)
        g_1_1.click()
        sleep(10)


if __name__ == '__main__':
    print('тест запускается с body_test.py')
