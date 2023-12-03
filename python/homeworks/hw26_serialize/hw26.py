import json
import random
from typing import List
from dataclasses import dataclass


@dataclass
class City:
    """
    Класс, представляющий информацию о городе.
    """
    name: str  # Название города
    district: str  # Район
    population: int  # Численность населения
    subject: str  # Субъект Российской Федерации


class DataValidator:
    @staticmethod
    def validate_data(cities: List[City]) -> List[City]:
        """
        Проверяет и фильтрует список объектов городов.

        Аргументы:
        - cities: List[City] - список объектов городов
        Возвращает:
        - List[City] - отфильтрованный список объектов городов
        """
        valid_cities = []
        for city in cities:
            if city.name[0].lower() not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
                continue
            if not isinstance(city.name, str) or not isinstance(city.population, int):
                continue
            city.name = city.name.capitalize()
            valid_cities.append(city)
        return valid_cities


class DataSerializer:
    @staticmethod
    def serialize_data(cities: List[City], filename: str):
        """
        Сериализует данные в формате JSON.

        Аргументы:
        - cities: List[City] - список объектов городов
        - filename: str - имя файла для сериализации
        """
        serialized_data = []
        for city in cities:
            serialized_data.append({
                'name': city.name,
                'district': city.district,
                'population': city.population,
                'subject': city.subject
            })
        with open(filename, 'w') as file:
            json.dump(serialized_data, file)


def load_cities(filename: str) -> List[City]:
    """
    Загружает данные о городах из файла.

    Аргументы:
    - filename: str - имя файла с данными о городах
    Возвращает:
    - List[City] - список объектов городов
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        cities = []
        for item in data:
            cities.append(City(
                name=item['name'],
                district=item['district'],
                population=item['population'],
                subject=item['subject']
            ))
        return cities


def start_game():
    """
    Начинает игру в города.
    """
    cities = load_cities('cities.json')
    random.shuffle(cities)

    # Инициализация игры и начального города
    game_over = False
    used_cities = []
    current_city = cities.pop()
    used_cities.append(current_city)

    while not game_over:
        # Ход пользователя
        user_input = input('Введите название города: ').title()
        user_city = find_city(user_input, cities)
        if user_input == 'Выход':
            print(f'Вы ввели "{user_input}"! Спасибо за игру!')
            break
        elif user_city is None:
            print(f'Города нет в списке или "{user_input}" уже был использован. Попробуйте ещё раз!')
            continue
        else:
            used_cities.append(user_city)
            cities.remove(user_city)
            current_city = user_city

        # Ход компьютера
        if current_city.name[-1] in ['ь', 'ы', 'й']:
            computer_city = find_city_by_letter(current_city.name[-2], cities)
        else:
            computer_city = find_city_by_letter(current_city.name[-1], cities)

        if computer_city is None:
            print('Компьютер не смог назвать город. Вы победили!')
            game_over = True
        elif computer_city.name[-1] in ['ь', 'ы', 'й']:
            second_last_letter = computer_city.name[-2]
            used_cities.append(computer_city)
            cities.remove(computer_city)
            current_city = computer_city
            print(f'Компьютер назвал город: {current_city.name}.\n'
                  f'Введите город на букву "{second_last_letter.upper()}".')
        else:
            used_cities.append(computer_city)
            cities.remove(computer_city)
            current_city = computer_city
            print(f'Компьютер назвал город: {current_city.name}')

        # Проверка окончания игры
        if len(cities) == 0:
            print('Все города использованы. Игра окончена!')
            game_over = True


def find_city(city_name: str, cities: List[City]) -> City:
    """
    Поиск города по имени.

    Аргументы:
    - city_name (str): Имя города для поиска.
    - cities (List[City]): Список городов, в котором нужно выполнить поиск.
    Возвращает:
    - city (City): Найденный город или None, если город не найден.
    """
    for city in cities:
        if city.name.lower() == city_name.lower():
            return city
    return None


def find_city_by_letter(letter: str, cities: List[City]) -> City:
    """
    Поиск города по первой букве имени.

    Аргументы:
    - letter (str): Первая буква имени города для поиска.
    - cities (List[City]): Список городов, в котором нужно выполнить поиск.
    Возвращает:
    - city (City): Найденный город или None, если город не найден.
    """
    for city in cities:
        if city.name[0].lower() == letter.lower():
            return city
    return None


print('Для выхода введите "Выход"!')
start_game()

input('\n\nНажмите "ENTER" для завершения.')
