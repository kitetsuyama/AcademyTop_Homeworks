import requests
from dataclasses import dataclass
from marshmallow import Schema, fields, ValidationError
from marshmallow_jsonschema import JSONSchema


@dataclass
class CurrentWeather:
    """
    Класс, описывающий текущую погоду
    """
    city: str  # город
    temperature: float  # температура
    feels_like: float  # ощущается как
    humidity: float  # влажность
    wind_speed: float  # скорость ветра
    description: str  # описание


class CurrentWeatherSchema(Schema):
    """
    Схема для валидации и сериализации данных о погоде
    """
    city = fields.Str(required=True)  # город
    temperature = fields.Float(required=True)  # температура
    feels_like = fields.Float(required=True)  # ощущается как
    humidity = fields.Float(required=True)  # влажность
    wind_speed = fields.Float(required=True)  # скорость ветра
    description = fields.Str(required=True)  # описание


def get_weather(city_name):
    """
    Получение данных о погоде
    :param city_name: название города
    :return: объект класса CurrentWeather
    """
    api_key = "23496c2a58b99648af590ee8a29c5348"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'lang': 'ru',
        'units': 'metric',
        'appid': api_key
    }
    response = requests.get(base_url, params=params)
    response_json = response.json()

    weather_data = CurrentWeather(
        city=city_name,
        temperature=response_json['main']['temp'],
        feels_like=response_json['main']['feels_like'],
        humidity=response_json['main']['humidity'],
        wind_speed=response_json['wind']['speed'],
        description=response_json['weather'][0]['description']
    )

    return weather_data


def validate_and_serialize(schema, data):
    """
    Валидация и сериализация данных
    :param schema: схема для валидации и сериализации данных
    :param data: данные для валидации и сериализации
    :return: сериализованные данные
    """
    try:
        schema.validate(data)
        serialized_data = schema.dump(data)
        return serialized_data
    except ValidationError as e:
        print(f"Ошибка валидации: {e.messages}")


def generate_json_schema(schema, filename):
    """
    Генерация JSON-схемы
    :param schema: схема для генерации JSON-схемы
    :param filename: имя файла для сохранения JSON-схемы
    """
    json_schema = JSONSchema().dump(schema)
    with open(filename, 'w') as file:
        file.write(str(json_schema))


# Запуск программы
if __name__ == "__main__":
    city = input("Введите город: ").title()

    weather_data = get_weather(city)
    weather_schema = CurrentWeatherSchema()

    serialized_data = validate_and_serialize(weather_schema, weather_data)
    if serialized_data:
        print(f"Погода в городе {serialized_data['city']}:\n"
              f"Температура на данный момент: {serialized_data['temperature']}°C, но ощущается как: {serialized_data['feels_like']}°C\n"
              f"Влажность составляет: {serialized_data['humidity']}%, а скорость ветра: {serialized_data['wind_speed']} м/с\n"
              f"В целом, в городе - {serialized_data['description'].title()}.")

    generate_json_schema(weather_schema, "weather_schema.json")


input('\n\nНажмите "ENTER" для завершения.')
