# Spectrology
Скрипт для сокрытия изображения (BMP 24-bit) в спектрограмме звукового файла.  
Главный репозиторий был заброшен и более не обновляется. В этом форке внесены необходимые правки для корректной работы скрипта.

## Использование

```
Использование: spectrology.py [-h] [-r] [-o OUTPUT] [-b BOTTOM] [-t TOP] [-p PIXELS] [-s SAMPLING] INPUT

Позиционные аргументы:
  INPUT                               Название избражения, которое будет сокрыто.

Необязательные аргументы:
  -h, --help                          Показать это сообщение и выйти.
  -r, --rotate                        Повернуть изображение на 90 градусов.
  -o OUTPUT, --output OUTPUT          Название выходного WAV файла. По умолчанию: out.wav.
  -b BOTTOM, --bottom BOTTOM          Нижнее значение диапазона частоты. По умолчанию: 200 Гц.
  -t TOP, --top TOP                   Высшее значение диапазона частоты. По умолчанию: 20000 Гц.
  -p PIXELS, --pixels PIXELS          Пикселей за секунду. По умолчанию: 30 Пикселей.
  -s SAMPLING, --sampling SAMPLING    Частота дискретизации. По умолчанию: 44100 Гц.
```

## Пример

```
python spectrology.py test.bmp --bottom 13000 --top 19000
```
![spectrogram](https://solusipse.net/blog/img/posts/audio-samples/7.png)

## Полезное

Для получения дополнительной информации об этой технике, см. [эту статью](https://solusipse.net/blog/post/basic-methods-of-audio-steganography-spectrograms/) (eng).

## Перевод и исправление
### [Digit4lSh4d0w](https://github.com/Digit4lSh4d0w)
