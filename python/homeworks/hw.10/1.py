# импортируем библиотеку json
import json

# импортируем список городов
from cities import cities

# записываем список городов в json
cities_json = json.dumps(cities, ensure_ascii=False, indent=4)
with open("cities.json", "w", encoding='UTF-8') as file:
    file.write(cities_json)

# читаем данные из json и загружаем датасета
with open("cities.json", "r", encoding='UTF-8') as file:
    cities_json = file.read()
cities = json.loads(cities_json)

# Выводим данные
for city in cities:
    print(city)


input('\nНажмите "ENTER" для завершения.')
