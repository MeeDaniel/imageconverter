# Что может этот код
1. Способен конвертировать изображения в консольный текст путём использования символов " ░▒▓" и символов изменения цвета.
2. Может кодировать и декодировать сгенерированные изображения

# Инструкция по использованию:
## Конвертация изображения:
1. Запустите `main.py`
2. Выберите первое действие (конвертация изображения)
3. Введтие название изображения (оно должно быть в папке проекта) либо абсолютный путь к файлу
4. Выберите размер изображения (рекомендуется выбирать третий пункт (подстройка по размеры консоли))
5. Дождитесь генерации изображения (обычно это занимает не больше секунды)
6. Нажмите на любую клавишу клавиатуры, чтобы увидеть ваше изображение
   Далее вам будет предложено сохранить ваше изображение в закодированном виде в файл `encoded_image.txt`
## Кодировка изображения:
1. Для начала конвертируйте его (инструкция выше вам в помощь)
2. Введите Y, когда вам предложат сохранить изображение
   Готово. Ваше изображение лежит в закодированном виде в `encoded_image.txt`
## Декодировка изображения:
1. Запустите `main.py`
2. Выберите второе действие (декодировка изображения)
3. Замените содержимое существующего файла `image_to_decode.txt` на своё. **ВАЖНО!** Не советую просто вставлять свой код в этот файл. Лучше скопируйте файл со своим закодированным изображением в папку проекта, затем удалите существующий `image_to_decode.txt` и переименнуйте свой файл в `image_to_decode.txt`. Иначе данные могут утеряться.
4. Дождитесь декодировки (обычно это занимает не больше секунды)
5. Готово!
