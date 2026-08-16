from abc import ABC, abstractmethod

class BaseProduct(ABC):
    '''Абстрактный метод'''

    @property
    @abstractmethod
    def price(self):
        pass


class LogMixin:
    """Миксин для логирования в терминале создания объектов."""
    def __init__(self, name, description, price, quantity):
        class_name = self.__class__.__name__
        print(f"{class_name}('{name}', '{description}', {price}, {quantity})")
        super().__init__(name, description, price, quantity)


class Product(LogMixin, BaseProduct):
    """Создает и инициирует класс"""

    name: str
    description: str
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("...")
        if type(self) is not type(other):
            raise TypeError("...")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
