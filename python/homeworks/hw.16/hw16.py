# Задание 1: Сделайте импорт full_dict из документа marvel.py
from marvel import full_dict
from pprint import pprint

# Задание 2: Пользовательский ввод, разбитие его на список, перевод в int или None, если введено не число
user_input = input("Введите цифры через пробел: ")
numbers = user_input.split()
converted_numbers = list(map(lambda x: int(x) if x.isdigit() else None, numbers))

# Задание 3: Если введено числа 1 - 42, создаст список из фильмов с подходящими id
filtered_dict = dict(filter(lambda item: item[0] in converted_numbers, full_dict.items()))

# Задание 4: Создает список имен из director
directors_set = {movie["director"] for movie in full_dict.values()}

# Задание 5: Делает копию full_dict, и преобразует year из int str
str_dict = {key: {**value, 'year': str(value['year'])} for key, value in full_dict.items()}

# Задание 6: Создает список, который содержит фильмы начинающие на букву 'Ч'
filtered_dict_startswith_ch = dict(filter(lambda item: item[1]["title"].startswith("Ч"), full_dict.items()))

print('Результаты:')
# Задание 7: Использование pprint
# Первым задание был import, решил выводить со второго задание, дабы не запутаться где что.
pprint({'Задание 2': converted_numbers})
pprint({'Задание 3': filtered_dict})
pprint({'Задание 4': directors_set})
pprint({'Задание 5': str_dict})
pprint({'Задание 6': filtered_dict_startswith_ch})


input('\nНажмите "ENTER" для завершения.')


# Мой ввод
# ванпис 3 5 28 2011 a4sd 8
