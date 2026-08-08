#from src.product import Product


class Category:
    '''Создает и инициирует класс'''
    name: str
    description: str
    products: list
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
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        if not self.__products:
            return "В категории нет товаров"

        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return result
