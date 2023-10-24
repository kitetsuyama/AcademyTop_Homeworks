import json
import random


class JsonFile:
    @staticmethod
    def read(filename: str) -> set[str]:
        """
        Читает JSON-файл и возвращает множество названий городов.
        :param filename: Имя читаемого JSON-файла.
        :return: Множество названий городов.
        """
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return {city['name'] for city in data}

    @staticmethod
    def write(filename: str, cities: set[str]) -> None:
        """
        Записывает множество названий городов в JSON-файл.
        :param filename: Имя записываемого JSON-файла.
        :param cities: Множество названий городов.
        :return: None
        """
        data = [{'name': city} for city in cities]
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)


class Cities:
    def __init__(self, city_data: set[str]):
        """
        Инициализирует объект Cities с множеством названий городов.
        :param city_data: Множество названий городов.
        """
        self.cities = list(city_data)

    def get_random_city(self) -> str:
        """
        Возвращает случайное название города из списка.
        :return: Случайное название города.
        """
        return random.choice(self.cities)

    def remove_city(self, city: str) -> None:
        """
        Удаляет город из списка.
        :param city: Город для удаления.
        :return: None
        """
        self.cities.remove(city)


class CityGame:
    def __init__(self, cities: Cities):
        """
        Инициализирует объект CityGame с объектом Cities.
        :param cities: Объект Cities.
        """
        self.cities = cities
        self.used_cities = set()
        self.current_city = None

    def start_game(self) -> None:
        """
        Начинает игру в города, случайно выбирая город.
        :return: None
        """
        self.current_city = self.cities.get_random_city()
        self.used_cities.add(self.current_city)
        print(f'Компьютер начинает с города {self.current_city}!')

    def human_turn(self, city_input: str) -> None:
        """
        Выполняет ход игрока в игре в города.
        :param city_input: Введенное игроком название города.
        :return: None
        """
        if city_input not in self.cities.cities:
            print('Такого города нет или он уже был использован!')
            return

        if not self.is_valid_city(city_input):
            print('Город должен начинаться на последнюю букву предыдущего города!')
            return

        self.cities.remove_city(city_input)
        self.used_cities.add(city_input)
        self.current_city = city_input
        self.computer_turn()

    def computer_turn(self) -> None:
        """
        Позволяет компьютеру сделать ход в игре в города.
        :return: None
        """
        available_cities = [city for city in self.cities.cities if self.is_valid_city(city)]
        if not available_cities:
            self.end_game()
            return

        computer_city = random.choice(available_cities)
        self.cities.remove_city(computer_city)
        self.used_cities.add(computer_city)
        self.current_city = computer_city
        if self.current_city[-1] == 'ь' or self.current_city[-1] == 'ы':
            print(f'Компьютер выбирает город {self.current_city}!\n'
                  f'Введите город на "{self.current_city[-2].upper()}"!')
        else:
            print(f'Компьютер выбирает город {self.current_city}!')

    def is_valid_city(self, city: str) -> bool:
        """
        Проверяет, является ли данное название города допустимым для игры.
        :param city: Название города для проверки.
        :return: True, если город допустим, иначе False.
        """
        if self.current_city[-1].lower() != 'ь' and self.current_city[-1].lower() == city[0].lower():
            return True
        elif self.current_city[-1].lower() == 'ь' and self.current_city[-2].lower() == city[0].lower():
            return True
        elif self.current_city[-1].lower() != 'ы' and self.current_city[-1].lower() == city[0].lower():
            return True
        elif self.current_city[-1].lower() == 'ы' and self.current_city[-2].lower() == city[0].lower():
            return True
        return False

    def end_game(self) -> None:
        """
        Завершает игру.
        :return: None
        """
        print('Игра окончена! Нет доступных городов для продолжения.')

    def save_game_state(self) -> None:
        """
        Сохраняет текущее состояние игры в файл.
        :return: None
        """
        with open('used_cities.json', 'w') as file:
            json.dump(list(self.used_cities), file)
        print('Состояние игры сохранено в файл used_cities.json!')

    def load_game_state(self) -> None:
        """
        Загружает состояние игры из файла used_cities.json. Если файл не найден, начинает новую игру.
        :return: None
        """
        try:
            with open('used_cities.json', 'r') as file:
                self.used_cities = set(json.load(file))
                last_city = list(self.used_cities)[-1]
                self.cities.remove_city(last_city)
                self.current_city = last_city
                print(f'Загружено состояние игры. Продолжаем с города {self.current_city}')
        except FileNotFoundError:
            print('Файл used_cities.json не найден. Начинаем новую игру.')


def display_game_result() -> None:
    """
    Выводит сообщение об окончании игры.
    :return: None
    """
    print('Игра окончена! Спасибо за игру!')


class GameManager:
    def __init__(self, cities_file: str):
        """
        Создает экземпляр класса GameManager.
        :param cities_file: путь к файлу с городами.
        """
        self.cities = Cities(JsonFile.read(cities_file))
        self.game = CityGame(self.cities)

    def __call__(self) -> None:
        """
        Вызывает метод run_game.
        :return: None
        """
        self.run_game()

    def run_game(self) -> None:
        """
        Запускает игру.
        :return: None
        """
        self.game.start_game()
        while True:
            city = input('Введите название города: ').title()
            if city == 'Выход':
                self.game.save_game_state()
                break
            self.game.human_turn(city)
            if self.game.current_city is None:
                break
        display_game_result()


cities_file = 'cities.json'
game_manager = GameManager(cities_file)
print('Для выхода введите "Выход"!')
game_manager()


input('\n\nНажмите "ENTER" для завершения.')


# -------------------------------------------------------------------------
# Мои вводы
#
# Для выхода введите "Выход"!
# Компьютер начинает с города Усолье-Сибирское!
# Введите название города: екатеринбург
# Компьютер выбирает город Горячий Ключ!
# Введите название города: чита
# Компьютер выбирает город Анадырь!
# Введите город на "Р"!
# Введите название города: рязань
# Компьютер выбирает город Нефтекамск!
# Введите название города: казань
# Компьютер выбирает город Невель!
# Введите город на "Л"!
# Введите название города: липецк
# Компьютер выбирает город Княгинино!
# Введите название города: омск
# Компьютер выбирает город Кинешма!
# Введите название города: анапа
# Компьютер выбирает город Адыгейск!
# Введите название города: керчь
# Компьютер выбирает город Чадан!
# Введите название города: выход
# Состояние игры сохранено в файл used_cities.json!
# Игра окончена! Спасибо за игру!
#
#
# Нажмите "ENTER" для завершения.

