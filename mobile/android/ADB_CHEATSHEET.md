# Полезные команды ADB (шпаргалка)
- Подключённые устройства: `adb devices`
- Снимок экрана: `adb shell screencap -p /sdcard/s1.png && adb pull /sdcard/s1.png`
- Запись видео: `adb shell screenrecord /sdcard/v1.mp4 && adb pull /sdcard/v1.mp4`
- Логи: `adb logcat -d > logcat.txt`
- Сеть OFF/ON: `adb shell svc wifi disable|enable`, `adb shell svc data disable|enable`
- Очистка данных приложения: `adb shell pm clear com.example.app`
