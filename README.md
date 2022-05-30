# spectrology
Скрипт для сокрытия изображения (BMP 24-bit) в спектрограмме звукового файла.  
Главный репозиторий был заброшен и более не обновляется. В этом форке внесены необходимые правки для корректной работы скрипта.

## Использование

```
usage: spectrology.py [-h] [-r] [-o OUTPUT] [-b BOTTOM] [-t TOP] [-p PIXELS]
                      [-s SAMPLING]
                      INPUT

positional arguments:
  INPUT                 Название избражения, которое будет сокрыто.

optional arguments:
  -h, --help            Показать это сообщение и выйти.
  -r, --rotate          Повернуть изображение на 90 градусов.
  -o OUTPUT, --output OUTPUT
                        Name of the output wav file. Default value: out.wav).
  -b BOTTOM, --bottom BOTTOM
                        Bottom frequency range. Default value: 200.
  -t TOP, --top TOP     Top frequency range. Default value: 20000.
  -p PIXELS, --pixels PIXELS
                        Pixels per second. Default value: 30.
  -s SAMPLING, --sampling SAMPLING
                        Sampling rate. Default value: 44100.
```

```
python spectrology.py test.bmp -b 13000 -t 19000
```
![spectrogram](https://solusipse.net/blog/img/posts/audio-samples/7.png)

For more informations on this techique, see this article: https://solusipse.net/blog/post/basic-methods-of-audio-steganography-spectrograms/.

## License
See `LICENSE`.
