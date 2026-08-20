import pytest

from src.category import Category
from src.product import Product


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(first_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 3
    assert second_category.product_count == 3


def test_category_add_product(first_category):
    """Тест: добавление продукта в категорию."""
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    old_count = first_category.product_count
    first_category.add_product(product4)

    assert len(first_category.products) == 3
    assert first_category.product_count == old_count + 1


def test_category_products_format(first_category):
    """Тест: формат вывода продуктов."""
    expected = ["Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.", "Iphone 15, 210000.0 руб. Остаток: 8 шт."]
    assert first_category.products == expected


def test_category_private_products():
    """Тест: продукты приватные (не доступны напрямую)."""
    product = Product("Product1", "Desc1", 100.0, 5)
    category = Category("Cat1", "Desc1", [product])

    with pytest.raises(AttributeError):
        category.__products


def test_category_str(first_category):
    """Тест: строковое представление категории."""
    # В первой категории 2 продукта: 5 + 8 = 13
    expected = "Смартфоны, количество продуктов: 13 шт."
    assert str(first_category) == expected


def test_category_str_empty():
    """Тест: строковое представление пустой категории."""
    category = Category("Пустая категория", "Описание", [])
    expected = "Пустая категория, количество продуктов: 0 шт."
    assert str(category) == expected


def test_category_middle_price():
    """Тест: средняя цена продуктов в категории."""
    product1 = Product("Product1", "Desc1", 100, 5)
    product2 = Product("Product2", "Desc2", 200, 3)
    category = Category("Cat", "Desc", [product1, product2])

    # (100 + 200) / (5 + 3) = 300 / 8 = 37.5
    assert category.middle_price() == 37.5


def test_category_middle_price_empty():
    """Тест: средняя цена в пустой категории (должен быть 0)."""
    category = Category("Empty", "Desc", [])
    assert category.middle_price() == 0
