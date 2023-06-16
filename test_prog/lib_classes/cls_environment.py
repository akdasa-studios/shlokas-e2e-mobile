
class Environment:
    version = '0.3 (beta)'

    @classmethod
    def enable_environment(cls):
        print(f'test prog version {cls.version}')
        print('создание окружения (запуск приложений, эмуляторов устройств и серверов, проверка их запуска) '
              '(не реализовано как и их отключение/пока запускать/выключать вручную.).')

    #TODO решить как запустить после теста. (по умолчанию выполняется перед тестом.)
    @classmethod
    def disable_environment(cls):
        print('освобождение ресурсов (закрытие приложений и их компонентов)')


if __name__ == '__main__':
    print('тест запускается с body_test.py')
