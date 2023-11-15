import json
from typing import List


class Palindrome:
    """
    Класс, представляющий палиндром.
    """

    def __init__(self, word: str, meaning: str):
        """
        Инициализирует экземпляр класса Palindrome.
        :param word: Слово палиндрома.
        :param meaning: Значение/определение палиндрома.
        """
        self.word = word  # Слово палиндрома
        self.meaning = meaning  # Значение/определение палиндрома

    def __bool__(self):
        """
        Проверяет, является ли слово палиндромом.
        :return: True, если слово является палиндромом, иначе False.
        """
        return self.word == self.word[::-1]  # Сравниваем слово с его перевёрнутой версией

    @classmethod
    def from_json(cls, data: dict) -> 'Palindrome':
        """
        Создаёт экземпляр класса Palindrome из словаря.
        :param data: Словарь данных палиндрома, содержащий ключи "слово" и "значение".
        :return: Экземпляр класса Palindrome.
        """
        return cls(data['слово'], data['значение'])  # Создаём экземпляр класса с переданными значениями


def main():
    """
    Основная функция программы.
    :return:
    """
    with open('palindromes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    palindromes: List[Palindrome] = [Palindrome.from_json(d) for d in data]
    palindrome_count = 0  # Счётчик палиндромов
    non_palindrome_count = 0  # Счётчик не-палиндромов
    for p in palindromes:
        if bool(p):
            palindrome_count += 1  # Увеличиваем счётчик палиндромов
        else:
            non_palindrome_count += 1  # Увеличиваем счётчик не-палиндромов
    print(f'Количество палиндромов: {palindrome_count}')
    print(f'Количество не-палиндромов: {non_palindrome_count}')


if __name__ == '__main__':
    main()


input('\n\nНажмите "ENTER" для завершения.')
