# ООП проект "Магазин"

Проект для изучения основ объектно-ориентированного программирования на Python.

## Описание

Проект представляет собой модель интернет-магазина с двумя основными классами:

- **Product** — товар с названием, описанием, ценой и количеством
- **Category** — категория товаров с названием, описанием и списком товаров

Класс `Category` автоматически подсчитывает общее количество категорий и товаров при создании новых объектов.

## Установка

1. Клонируйте репозиторий:

git clone https://github.com/olegmokhovural-sys/oop.git
cd oop
Установите зависимости:

poetry install

## Использование

Пример создания товаров и категорий:

python
from src.product import Product
from src.category import Category

## Создание товаров
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

## Создание категории
category = Category("Смартфоны", "Описание категории", [product1, product2])

## Вывод информации
print(category.name)
print(category.category_count)  # общее количество категорий
print(category.product_count)   # общее количество товаров
Тестирование
Для запуска тестов используйте:

pytest
Для проверки покрытия кода тестами:

pytest --cov=src tests/