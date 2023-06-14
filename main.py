from class_test import TestObj

import lib_block_tests as lbt
import lib_config as lc


def main():
    test = TestObj({'conf': lc.config_00, 'list_test': [lbt.test_001]})
    if test.check_create_test_obj():
        print('Запущены все приложения, драйвер и список тестов корректны.')
        print('Начало теста.')
        test.run_test()
    else:
        print('Не запущены все приложения или конфигурация драйвера или тесты не корректны.')


if __name__ == '__main__':
    main()
