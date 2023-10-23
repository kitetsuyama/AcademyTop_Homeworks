import csv


def password_validator(length: int = 8, uppercase: int = 1, lowercase: int = 1, special_chars: int = 1):
    """
    Декоратор для валидации паролей.
    Параметры:
    length (int): Минимальная длина пароля (по умолчанию 8).
    uppercase (int): Минимальное количество букв верхнего регистра (по умолчанию 1).
    lowercase (int): Минимальное количество букв нижнего регистра (по умолчанию 1).
    special_chars (int): Минимальное количество спец-знаков (по умолчанию 1).
    """

    def wrapper(func):
        def inner(username: str, password: str):
            if len(password) < length:
                raise ValueError(f'Пароль должен быть не менее {length} символов!')
            if sum(1 for c in password if c.isupper()) < uppercase:
                raise ValueError(f'Пароль должен содержать не менее {uppercase} заглавных букв!')
            if sum(1 for c in password if c.islower()) < lowercase:
                raise ValueError(f'Пароль должен содержать не менее {lowercase} строчных букв!')
            if sum(1 for c in password if not c.isalnum()) < special_chars:
                raise ValueError(f'Пароль должен содержать не менее {special_chars} спец-символов!')
            return func(username, password)

        return inner

    return wrapper


def username_validator():
    """
    Декоратор для валидации имени пользователя.
    """

    def wrapper(func):
        def inner(username: str, password: str):
            if ' ' in username:
                raise ValueError('Имя пользователя не должно содержать пробелы!')
            return func(username, password)

        return inner

    return wrapper


@password_validator(length=10, uppercase=2, lowercase=2, special_chars=2)
@username_validator()
def register_user(username: str, password: str):
    """ Функция для регистрации нового пользователя.
    Параметры:
    username (str): Имя пользователя.
    password (str): Пароль пользователя.
    Raises:
    ValueError: Если пароль или юзернейм не соответствует заданным условиям.
    """
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])


# ----------------------------------------------------------------------------
# Ошибка: Пароль должен быть не менее 10 символов
try:
    register_user('AlexTim', "qweasdzxc")
    print('\nРегистрация прошла успешно!')
except ValueError as e:
    print(f'\n  Ошибка: \n{e}')


# Ошибка: Пароль должен содержать не менее 2 заглавных букв
try:
    register_user("AlexTim", "qweasd123!!!")
    print('\nРегистрация прошла успешно!')
except ValueError as e:
    print(f'\n  Ошибка: \n{e}')


# Ошибка: Пароль должен содержать не менее 2 строчных букв
try:
    register_user('AlexTim', 'QWEASD123!!!')
    print('\nРегистрация прошла успешно!')
except ValueError as e:
    print(f'\n  Ошибка: \n{e}')


# Ошибка: Пароль должен содержать не менее 2 спец-символов
try:
    register_user('AlexTim', 'qweASD123!')
    print('\nРегистрация прошла успешно!')
except ValueError as e:
    print(f'\n  Ошибка: \n{e}')


# Ошибка: Имя пользователя не должно содержать пробелы
try:
    register_user('Alex Tim', 'qweASD123!!!')
    print('\nРегистрация прошла успешно!')
except ValueError as e:
    print(f'\n  Ошибка: \n{e}')


# Регистрация прошла успешно!
try:
    register_user('AlexTim', 'qweASD123!!')
    print('\nРегистрация прошла успешно!')
except ValueError as e:
    print(f'\n  Ошибка: \n{e}')


# Проверка mypy
# (venv) PS D:\1ucheba\PycharmProjects\pyExp> mypy .\1homework\hw.20_07.10.23\hw20.py
# Success: no issues found in 1 source file
