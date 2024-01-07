import pytest


# Определение класса WeatherRequest для запроса погоды
class WeatherRequest:
    def __init__(self, city=None):
        self.city = city  # Устанавливаем значение city
        # Инициализация других параметров класса

    def get_weather(self):
        # Логика получения погоды
        pass  # Заглушка, реализация логики получения погоды


# Фикстура для создания объекта WeatherRequest с городом Москва
@pytest.fixture(scope='module')
def weather_request():
    return WeatherRequest(city='Москва')


# Фикстура для создания объекта WeatherRequest без указания города
@pytest.fixture(scope='module')
def weather_request_parametrize():
    return WeatherRequest()


# Список городов и их ожидаемых координат
cities = [
    ('Москва', {"lon": 37.6156, "lat": 55.7522}),
    ('Воронеж', {"lon": 39.17, "lat": 51.6664}),
    ('Санкт-Петербург', {"lon": 30.2642, "lat": 59.8944}),
    ('Краснодар', {"lon": 38.9769, "lat": 45.0328}),
    ('Сочи', {"lon": 39.7303, "lat": 43.6}),
]


# Параметризованный тест для проверки координат городов
@pytest.mark.parametrize('city_name, expected_coords', cities)
def test_weather_request_city_coodrd_name_parametrize(weather_request_parametrize, city_name, expected_coords):
    weather_request_parametrize.city = city_name
    coords = weather_request_parametrize.get_weather()
    assert coords == expected_coords


# Тест для проверки названия города в ответе
def test_weather_request_city_name(weather_request):
    city = weather_request.city
    response = weather_request.get_weather()
    assert response['name'] == city


# Тест для проверки координат в ответе
def test_weather_request_coord(weather_request):
    expected_coords = {"lon": 37.6156, "lat": 55.7522}
    response = weather_request.get_weather()
    assert response['coord'] == expected_coords


# Тест для проверки наличия ключей в разделе 'weather' в ответе
def test_weather_request_weather_key(weather_request):
    response = weather_request.get_weather()
    assert 'weather' in response
    assert 'id' in response['weather']
    assert 'main' in response['weather']
    assert 'description' in response['weather']
    assert 'icon' in response['weather']


# Тест для проверки наличия ключей в разделе 'main' в ответе
def test_weather_request_main_key(weather_request):
    response = weather_request.get_weather()
    assert 'main' in response
    assert 'temp' in response['main']
    assert 'feels_like' in response['main']
    assert 'temp_min' in response['main']
    assert 'temp_max' in response['main']
    assert 'pressure' in response['main']
    assert 'humidity' in response['main']
