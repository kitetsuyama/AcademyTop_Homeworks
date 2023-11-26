"""
Домашнее задание №23

Релизация классов для доставки товара, с учетом международной доставки и промо-кодов
Использование миксинов для расширения функционала классов а так же dataclass для хранения промо-кодов
"""

from dataclasses import dataclass
import json
from typing import List, Tuple, Union


# 1. Базовые классы:
class Product:
    """
    Базовый класс для товара
    """
    def __init__(self, dimensions: Tuple[float, float, float], weight: float, fragility: bool, price: float,
                 category: str, name: str):
        self.dimensions = dimensions
        self.weight = weight
        self.fragility = fragility
        self.price = price
        self.category = category
        self.name = name


class Delivery:
    """
    Базовый класс для доставки
    """
    def __init__(self, delivery_speed: int):
        self.delivery_speed = delivery_speed

    def calculate_cost(self, product: Product) -> float:
        # Базовая формула
        return product.price * 0.01 + product.weight * 0.05


# 2. Датаклассы:
@dataclass
class PromoCodeData:
    """
    Датакласс для хранения промо-кода
    """
    code: str
    discount: int

    @classmethod
    def load_from_json(cls, json_path: str) -> List['PromoCodeData']:
        """
        Метод для загрузки промо-кодов из json
        :param json_path:
        :return:
        """
        with open(json_path, 'r') as f:
            data = json.load(f)
            return [cls(code=item['code'], discount=item['discount']) for item in data]


# 3. Миксины:
class InternationalMixin:
    """
    Миксин для международной доставки
    Добавляет дополнительные расходы и условия для международной доставки
    """
    def adjust_for_weight(self, product: Product) -> float:
        """
        Метод для расчета дополнительных расходов на доставку в зависимости от веса
        :param product: Объект товара
        :return: Дополнительные расходы на доставку
        """
        return product.weight * 0.1

    def adjust_for_dimensions(self, product: Product) -> float:
        """
        Метод для расчета дополнительных расходов на доставку в зависимости от габаритов
        :param product: Объект товара
        :return: Дополнительные расходы на доставку
        """
        return sum(product.dimensions) * 0.05

    def adjust_for_fragility(self, product: Product) -> float:
        """
        Метод для расчета дополнительных расходов на доставку в зависимости от хрупкости
        :param product: Объект товара
        :return: Дополнительные расходы на доставку
        """
        return product.price * 0.05 if product.fragility else 0


class SortByCostMixin:
    @staticmethod
    def sort_by_price_ascending(services: List[Tuple['Delivery', float]]) -> List[Tuple['Delivery', float]]:
        return sorted(services, key=lambda x: x[1])

    @staticmethod
    def sort_by_price_descending(services: List[Tuple['Delivery', float]]) -> List[Tuple['Delivery', float]]:
        return sorted(services, key=lambda x: x[1], reverse=True)

    @staticmethod
    def sort_by_delivery_speed(services: List[Tuple['Delivery', float]]) -> List[Tuple['Delivery', float]]:
        return sorted(services, key=lambda x: x[0].delivery_speed)


# 4. Специализированные классы доставки:
class DeliveryServiceA(Delivery):
    """
    Класс для доставки сервисом A
    """
    def calculate_cost_for_service(self, product: Product) -> float:
        return self.calculate_cost(product) + 10


class DeliveryServiceB(Delivery, InternationalMixin):
    """
    Класс для доставки сервисом B. У него есть
    международная доставка, поэтому мы используем миксин InternationalMixin
    """
    def calculate_cost_for_service(self, product: Product) -> float:
        cost = self.calculate_cost(product)
        cost += self.adjust_for_weight(product)
        cost += self.adjust_for_dimensions(product)
        cost += self.adjust_for_fragility(product)
        return cost + 20


class DeliveryServiceC(Delivery, InternationalMixin):
    """
    Класс для доставки сервисом C. У него есть
    международная доставка, поэтому мы используем миксин InternationalMixin
    """
    def calculate_cost_for_service(self, product: Product) -> float:
        cost = self.calculate_cost(product)
        cost += self.adjust_for_weight(product) * 2
        cost += self.adjust_for_dimensions(product) * 2
        cost += self.adjust_for_fragility(product) * 2
        return cost + 30


# 5. Логика промо-кода:
class PromoCodeMixin:
    """
    Миксин для применения промо-кода
    """
    @staticmethod
    def apply_promo_code(self, promo_code: str, cost: float, promo_codes: List[PromoCodeData]) -> float:
        for code in promo_codes:
            if code.code == promo_code:
                return cost * (1 - code.discount / 100)
        return cost


def main():
    # Создаем товар
    product = Product((10, 10, 10), 2, True, 100, "Electronics", "Camera")

    # Создаем сервисы доставки
    serviceA = DeliveryServiceA(3)
    serviceB = DeliveryServiceB(5)
    serviceC = DeliveryServiceC(4)

    # Создаем список сервисов доставки
    services = [serviceA, serviceB, serviceC]

    # Загружаем промо-коды
    promo_codes = PromoCodeData.load_from_json("../data/promocodes.json")

    # Считаем стоимость доставки для каждого сервиса
    costs = []
    for service in services:
        cost = service.calculate_cost_for_service(product)
        cost_with_promo = PromoCodeMixin.apply_promo_code(service, "promo", cost, promo_codes)
        costs.append((service, cost_with_promo))

    # Сортируем по цене и по скорости доставки
    sorted_by_price = SortByCostMixin.sort_by_price_ascending(costs)
    sorted_by_speed = SortByCostMixin.sort_by_delivery_speed(costs)

    print("Sorted by Price:")
    for service, cost in sorted_by_price:
        print(f"{service.__class__.__name__}: ${cost:.2f}")

    print("\nSorted by Delivery Speed:")
    for service, cost in sorted_by_speed:
        print(f"{service.__class__.__name__}: {service.delivery_speed} days")


if __name__ == "__main__":
    main()
