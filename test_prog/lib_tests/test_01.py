from test_prog.lib_classes.cls_test import BaseTest


class Test(BaseTest):
    def test_name(self):
        self.assertEqual(self.prog('Иван'), 'Hello, иван!')


if __name__ == '__main__':
    print('тест запускается с body_test.py')
