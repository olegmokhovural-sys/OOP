import pytest

from src.product import Product


def test_product_init(product):
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_product_price_getter():
    """Тест: геттер цены."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    assert product.price == 180000.0


def test_product_price_setter_valid():
    """Тест: установка корректной цены."""
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product.price = 30000.0
    assert product.price == 30000.0


def test_product_price_setter_negative(capsys):
    """Тест: установка отрицательной цены (цена не меняется)."""
    product = Product("Test", "Description", 100.0, 5)
    product.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100.0


def test_product_new_product():
    """Тест: создание продукта через класс-метод new_product."""
    data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    product = Product.new_product(data)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_private_price():
    """Тест: цена приватная (не доступна напрямую)."""
    product = Product("Test", "Description", 100.0, 5)
    with pytest.raises(AttributeError):
        product.__price


def test_product_str(product):
    """Тест: строковое представление продукта."""
    expected = "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(product) == expected


def test_product_add():
    """Тест: сложение продуктов (стоимость на складе)."""
    product_a = Product("Товар A", "Описание", 100, 10)
    product_b = Product("Товар B", "Описание", 200, 2)
    result = product_a + product_b
    assert result == 100 * 10 + 200 * 2  # 1400


def test_product_add_wrong_type():
    """Тест: сложение с неправильным типом (должен быть TypeError)."""
    product = Product("Товар A", "Описание", 100, 10)
    try:
        result = product + 5
        assert False, "Ожидалась ошибка TypeError"
    except TypeError:
        assert True


def test_product_add_different_classes():
    """Тест: сложение товаров разных классов (должен быть TypeError)."""
    from src.product import Smartphone, LawnGrass

    phone = Smartphone("iPhone 15", "...", 100000, 10, 0.9, "Pro", 256, "Black")
    grass = LawnGrass("Газон", "...", 500, 100, "Россия", 30, "Зелёный")

    try:
        result = phone + grass
        assert False, "Ожидалась ошибка TypeError"
    except TypeError:
        assert True


def test_product_inherits_base():
    """Тест: Product наследует BaseProduct."""
    from src.product import Product, BaseProduct

    product = Product("Test", "Desc", 100, 5)
    assert isinstance(product, BaseProduct)


def test_product_implements_price():
    """Тест: Product реализует абстрактный метод price."""
    from src.product import Product

    product = Product("Test", "Desc", 100, 5)
    assert product.price == 100


def test_log_mixin_output():
    """Тест: миксин выводит логи при создании объекта."""
    from src.product import Product

    product = Product("Тестовый продукт", "Тестовое описание", 500, 10)
    assert product.price == 500
    assert product.quantity == 10


def test_log_mixin_in_smartphone():
    """Тест: миксин работает при создании Smartphone."""
    from src.product import Smartphone

    phone = Smartphone("iPhone 15", "Флагман", 100000, 10, 0.9, "Pro", 256, "Black")
    assert phone.price == 100000
    assert phone.quantity == 10
    assert phone.model == "Pro"


def test_product_zero_quantity():
    """Тест: создание продукта с нулевым количеством (должен быть ValueError)."""
    try:
        product = Product("Test", "Desc", 100, 0)
        assert False, "Ожидалась ошибка ValueError"
    except ValueError:
        assert True
