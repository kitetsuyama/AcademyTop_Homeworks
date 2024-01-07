# Абстрактный класс IngredientFactory
class IngredientFactory:
    def create_cheese(self) -> str:  # Метод создания сыра (абстрактный)
        pass

    def create_sauce(self) -> str:  # Метод создания соуса (абстрактный)
        pass


# Класс DodoIngredientFactory, наследуется от IngredientFactory
class DodoIngredientFactory(IngredientFactory):
    def create_cheese(self) -> str:  # Реализация метода создания сыра для Dodo
        return "Сыром Додо Пиццы"

    def create_sauce(self) -> str:  # Реализация метода создания соуса для Dodo
        return "Соусом Додо Пиццы"


# Класс SizeFactory
class SizeFactory:
    def create_size(self, size: str) -> str:  # Метод создания размера пиццы
        if size == "Маленькая":
            return "Пицца маленького размера"
        elif size == "Средняя":
            return "Пицца среднего размера"
        elif size == "Большая":
            return "Пицца большого размера"
        else:
            return "Неверный размер"


# Класс PizzaBuilder
class PizzaBuilder:
    def __init__(self, ingredient_factory: IngredientFactory, size_factory: SizeFactory):
        self.ingredient_factory = ingredient_factory
        self.size_factory = size_factory

    def build_pizza(self, size: str) -> str:  # Метод построения пиццы
        cheese = self.ingredient_factory.create_cheese()  # Создание сыра
        sauce = self.ingredient_factory.create_sauce()  # Создание соуса
        pizza_size = self.size_factory.create_size(size)  # Создание размера пиццы

        pizza = f"Пицца с {cheese} и {sauce}, {pizza_size}"  # Соединение всех ингредиентов
        return pizza


# Пример использования классов и методов
ingredient_factory = DodoIngredientFactory()
size_factory = SizeFactory()
pizza_builder = PizzaBuilder(ingredient_factory, size_factory)

size = input("Введите размер пиццы (Маленькая, Средняя, Большая): ").title()
pizza = pizza_builder.build_pizza(size)
print(pizza)