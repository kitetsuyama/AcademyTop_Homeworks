from typing import Callable


def password_checker(func: Callable) -> Callable:
    """
    Декоратор для проверки сложности пароля.
    :param func: Функция, которую нужно декорировать
    :return: Декорированная функция
    """
    def wrapper(password: str) -> str:
        """
        Функция для проверки сложности пароля.
        :param password: Пароль для проверки
        :return: Сообщение об ошибке или результат выполнения функции func
        """
        if len(password) < 8:
            return 'Пароль должен содержать не менее 8 символов'
        elif ' ' in password:
            return 'Пароль не должен содержать пробелы'
        elif not any(char.isdigit() for char in password):
            return 'Пароль должен содержать хотя бы одну цифру'
        elif not any(char.isupper() for char in password):
            return 'Пароль должен содержать хотя бы одну заглавную букву'
        elif not any(char.islower() for char in password):
            return 'Пароль должен содержать хотя бы одну строчную букву'
        elif not any(char in "!@#$%^&*()-+?_=,<>/" for char in password):
            return 'Пароль должен содержать хотя бы один спецсимвол'
        else:
            return func(password)
    return wrapper


@password_checker
def register_user(password: str) -> str:
    """
    Функция для регистрации пользователя.
    :param password: Пароль пользователя
    :return: Сообщение об успешной регистрации
    """
    return "Пользователь успешно зарегистрирован"


# Примеры использования декоратора для проверки сложности пароля
print(register_user('qweasd'))        # Пароль должен содержать не менее 8 символов
print(register_user('qweASD 123!'))   # Пароль не должен содержать пробелы
print(register_user('qweasdzxc'))     # Пароль должен содержать хотя бы одну цифру
print(register_user('qweasd123'))     # Пароль должен содержать хотя бы одну заглавную букву
print(register_user('QWEASD123'))     # Пароль должен содержать хотя бы одну строчную букву
print(register_user('qweASD123'))     # Пароль должен содержать хотя бы один спецсимвол
print(register_user('qweASD123!@#'))  # Пользователь успешно зарегистрирован


input('\n\nНажмите "ENTER" для завершения.')


# Результат проверки mypy
# (venv) PS D:\1ucheba\PycharmProjects\pyExp> mypy .\1homework\hw.19_01.10.23\hw19.py
# Success: no issues found in 1 source file

