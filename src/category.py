from src.product import Product


class Category:
    """Создает и инициирует класс"""

    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product):
        """
        Метод для добавления товара в категорию.
        """
        if not isinstance(product, Product):
            raise TypeError(
                f"Можно добавлять только объекты класса Product или его наследников. "
                f"Получен: {type(product).__name__}"
            )
        self.__products.append(product)
        Category.product_count += 1

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def middle_price(self):
        """Возвращает среднюю цену продуктов в категории."""
        if not self.__products:
            return 0
        total_price = sum(product.price for product in self.__products)
        total_quantity = sum(product.quantity for product in self.__products)
        if total_quantity == 0:
            return 0
        return total_price / total_quantity

    @property
    def products(self):
        if not self.__products:
            return "В категории нет товаров"

        # result = []
        # for product in self.__products:
        #     result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        # return result

        return [str(product) for product in self.__products]
