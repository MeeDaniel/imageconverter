TITLE = """КОНВЕРТЕР ИЗОБРАЖЕНИЙ В ТЕКСТ, А ТАК ЖЕ КОДИРОВЩИК
(Используйте $home чтобы попасть на главную страницу, $exit чтобы закрыть окно)

"""
MAIN_PAGE = """~ ГЛАВНАЯ СТРАНИЦА

Выберите действие:
1. Превратить и изображение в текст
2. Декодировать изображение
> """
READ_NORMAL_IMAGE_ACTION_STAGE_1 = """~ Конвертация изображения в текст

Введите имя файла
> """
READ_NORMAL_IMAGE_ACTION_STAGE_2 = """
Выберите действие
1. Адаптировать под заданную ширину (сохраняя соотношение сторон)
2. Адаптировать под заданную высоту (сохраняя соотношение сторон)
3. Адаптировать под размеры консоли (Рекомендуется)
4. Не изменять размер изображения (Крайне не рекомендуется)
> """
READ_NORMAL_IMAGE_ACTION_STAGE_2_1 = """
Введите ширину
> """
READ_NORMAL_IMAGE_ACTION_STAGE_2_2 = """
Введите высоту
> """
READ_NOMRAL_IMAGE_ACTION_STAGE_3 = """
Генерируем текст..."""
READ_NORMAL_IMAGE_ACTION_STAGE_4 = """Изображение было сконвертированно. Хотите его увидеть?"""
READ_NORMAL_IMAGE_ACTION_STAGE_5 = """Закодировать текст в файл `encoded_image.txt`? (Y/N)
> """
READ_NORMAL_IMAGE_ACTION_GOBACK = """Что-то пошло не так..."""

DECODE_IMAGE_STAGE_1 = """~ Декодировка изображения

Для начала замените файл `image_to_decode.txt` на файл с вашим закодированным изображением (не забудьте переименновать его). Нажмите любую кнопку, когда будете готовы."""
DECODE_IMAGE_STAGE_2 = """Декодируем ваше изображение..."""
DECODE_IMAGE_STAGE_3 = """Готово! Теперь вам нужно изменить ширину консоли до {} символов или больше. (Это важно)"""

WRONG_ACTION__INCORRECT_NUMBER = "Пожалуйста, укажите одно из предложенных действий. Здесь нет действия \"{}\"."
WRONG_ACTION__NOT_A_NUMBER = "Пожалуйста, укажите число (type: int)."
WRONG_INT__NOT_A_NUMBER = "Пожалуйста, введите целое число."