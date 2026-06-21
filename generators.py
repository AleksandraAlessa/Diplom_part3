import random
import string

def generate_unique_email():
    """
    Генерирует email в формате: имя_фамилия_номер_когорты_3цифры@домен
    Пример: aleksandra_usova_46_123@yandex.ru
    (замените на свои данные)
    """
    first_name = "aleksandra"          # ваше имя
    last_name = "usova"        # ваша фамилия
    cohort = "46"                 # номер когорты (спринт 5)
    random_digits = ''.join(random.choices(string.digits, k=3))
    return f"{first_name}_{last_name}_{cohort}_{random_digits}@yandex.ru"
