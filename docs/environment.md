# Установка окружения

0. Скачать репозиторий `git clone https://github.com/akdasa-studios/shlokas-e2e-mobile.git`
1. Установить [Android Studio](https://developer.android.com/)
2. Установить [Node](https://nodejs.org/en)
3. Установить [Appium](https://appium.io/docs/en/2.0/quickstart/install/)
4. Усановить [Python](https://www.python.org/downloads/)
5. `pip install -r requirements.txt`
6. Установить переменную окружения `ANDROID_HOME` - путь до Android SDK
7. Установить переменную окружения `JAVA_HOME` - путь до Java JDK
8. Скачать последнюю версию APK приложения и положить в папку с проектом.


# Запуск окружения

0. Запустить appium в терминале `appium`
1. Запустить эмулятор в Android Studio: `Tools -> Device Manager`. Выбрать устройство `Pixel 5 API 33` и нажать `Play`
2. `python ./interactive.py`
