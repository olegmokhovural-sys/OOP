import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """Функция для чтения файла"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def make_data_of_json(data):
    """Преобразует JSON-данные в объекты Category и Product."""
    categories = []

    for category_data in data:
        products = []

        for product_data in category_data["products"]:
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            products.append(product)

        category = Category(name=category_data["name"], description=category_data["description"], products=products)
        categories.append(category)

    return categories


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    cat_data = make_data_of_json(raw_data)

    for category in cat_data:
        print(f"Категория: {category.name}")
        print(f"  Товаров: {len(category.products)}")
        for product in category.products:
            print(f"    - {product.name}: {product.price} руб.")
        print()
