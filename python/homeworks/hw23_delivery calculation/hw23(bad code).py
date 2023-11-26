from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    dimensions: str  # Размеры
    weight: float  # Вес
    fragility: bool  # Хрупкость
    price: float  # Цена
    category: str  # Категория
    name: str  # Наименование


@dataclass
class PromoCodeData:
    code: str  # Промо-код
    discount: int  # Скидка

    @staticmethod
    def load_from_json(json_path: str) -> List['PromoCodeData']:
        """
        Загружает данные о промокодах из JSON-файла.

        :param json_path: путь к JSON-файлу с данными о промокодах
        :return: список объектов PromoCodeData
        """
        pass


class InternationalMixin:
    def adjust_for_weight(self, cost: float) -> float:
        """
        Рассчитывает стоимость доставки с учетом веса товара.

        :param cost: стоимость доставки
        :return: стоимость доставки с учетом веса товара
        """
        pass

    def adjust_for_dimensions(self, cost: float) -> float:
        """
        Рассчитывает стоимость доставки с учетом размеров товара.

        :param cost: стоимость доставки
        :return: стоимость доставки с учетом размеров товара
        """
        pass

    def adjust_for_fragility(self, cost: float) -> float:
        """
        Рассчитывает стоимость доставки с учетом хрупкости товара.

        :param cost: стоимость доставки
        :return: стоимость доставки с учетом хрупкости товара
        """
        pass


class SortByCostMixin:
    @staticmethod
    def sort_by_price_ascending(delivery_options: List['Delivery'], product: Product) -> List['Delivery']:
        """
        Сортирует список вариантов доставки по возрастанию стоимости.

        :param delivery_options: список объектов Delivery
        :param product: объект Product
        :return: отсортированный список объектов Delivery
        """
        return sorted(delivery_options, key=lambda delivery: delivery.calculate_cost(product) or float('inf'))

    @staticmethod
    def sort_by_price_descending(delivery_options: List['Delivery'], product: Product) -> List['Delivery']:
        """
        Сортирует список вариантов доставки по убыванию стоимости.

        :param delivery_options: список объектов Delivery
        :param product: объект Product
        :return: отсортированный список объектов Delivery
        """
        return sorted(delivery_options, key=lambda delivery: delivery.calculate_cost(product) or float('inf'), reverse=True)

    @staticmethod
    def sort_by_delivery_speed(delivery_options: List['Delivery']) -> List['Delivery']:
        """
        Сортирует список вариантов доставки по скорости доставки.

        :param delivery_options: список объектов Delivery
        :return: отсортированный список объектов Delivery
        """
        return sorted(delivery_options, key=lambda delivery: delivery.delivery_speed)


class PromoCodeMixin:
    def apply_promo_code(self, promo_code: str) -> None:
        """
        Применяет промокод к стоимости доставки.

        :param promo_code: строка с промокодом
        """
        pass


@dataclass
class Delivery:
    delivery_speed: str

    def calculate_cost(self, product: Product) -> float:
        """
        Рассчитывает стоимость доставки.

        :param product: объект Product
        :return: стоимость доставки
        """
        pass


class DeliveryServiceA(Delivery):
    def calculate_cost(self, product: Product) -> float:
        """
        Рассчитывает стоимость доставки для сервиса A.

        :param product: объект Product
        :return: стоимость доставки
        """
        return 10.0


class DeliveryServiceB(Delivery, InternationalMixin):
    def calculate_cost(self, product: Product) -> float:
        """
        Рассчитывает стоимость доставки для сервиса B.

        :param product: объект Product
        :return: стоимость доставки
        """
        return 15.0


class DeliveryServiceC(Delivery, InternationalMixin):
    def calculate_cost(self, product: Product) -> float:
        """
        Рассчитывает стоимость доставки для сервиса C.

        :param product: объект Product
        :return: стоимость доставки
        """
        return 20.0


def main() -> None:
    """
    Основная функция программы.
    """
    product: Product = Product(dimensions="10x10x10", weight=1.5, fragility=False, price=100.0, category="Electronics",
                               name="Smartphone")

    delivery_options: List[Delivery] = [
        DeliveryServiceA(delivery_speed="Standard"),
        DeliveryServiceB(delivery_speed="Express"),
        DeliveryServiceC(delivery_speed="Economy")
    ]

    promo_code: str = "DISCOUNT10"
    for delivery in delivery_options:
        if isinstance(delivery, PromoCodeMixin):
            delivery.apply_promo_code(promo_code)

    sorted_delivery_options: List[Delivery] = SortByCostMixin.sort_by_price_ascending(delivery_options, product)

    for delivery in sorted_delivery_options:
        cost: float = delivery.calculate_cost(product)
        print(f"Delivery Service: {delivery.__class__.__name__}")
        print(f"Delivery Cost: {cost}")
        print("------------")


if __name__ == "__main__":
    main()

input('\n\nНажмите "ENTER" для завершения.')
