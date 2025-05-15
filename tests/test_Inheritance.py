import pytest
from src.class2 import Product  # Убедитесь, что импорт корректен
from src.Inheritance import (
    Smartphone,
    LawnGrass,
)


@pytest.fixture
def setup_products():
    """Создаем объекты для тестирования"""
    smartphone1 = Smartphone(name="Смартфон A", price=500.00, quantity=5)
    smartphone2 = Smartphone(name="Смартфон B", price=500.00, quantity=5)
    lawn_grass = LawnGrass(name="Газонная трава", price=100.00, quantity=10)
    return smartphone1, smartphone2, lawn_grass


def test_smartphone_initialization(setup_products):
    smartphone1, _, _ = setup_products
    assert smartphone1.name == "Смартфон A"
    assert smartphone1.price == 500.00
    assert smartphone1.quantity == 5


def test_add_products_same_type(setup_products):
    smartphone1, smartphone2, _ = setup_products
    total_product = smartphone1 + smartphone2
    assert total_product.name == "Суммарный товар"
    # Средняя цена при сложении одинаковых цен остается той же
    assert total_product.price == 500.00
    assert total_product.quantity == 10


def test_add_products_different_type(setup_products):
    _, _, lawn_grass = setup_products
    smartphone1, _, _ = setup_products
    with pytest.raises(TypeError):
        _ = smartphone1 + lawn_grass


def test_add_invalid_product(setup_products):
    smartphone1, _, _ = setup_products
    with pytest.raises(TypeError):
        smartphone1.add_product("Некорректный продукт")


def test_add_valid_product(setup_products):
    smartphone1, smartphone2, _ = setup_products
    # Перед добавлением убедимся, что products пустой или не содержит этот продукт
    # Предположим, что products изначально пустой список
    if not hasattr(smartphone1, "products"):
        # Если в вашей реализации products не объявлен явно,
        # добавьте его или создайте для теста.
        setattr(smartphone1, "products", [])

    initial_count = len(smartphone1.products) if hasattr(smartphone1, "products") else 0

    # Добавляем продукт
    smartphone1.add_product(smartphone2)

    # Проверяем наличие продукта в списке продуктов
    assert hasattr(smartphone1, "products")
    assert smartphone2 in smartphone1.products
    assert len(smartphone1.products) == initial_count + 1


def test_new_product_creation():
    product_data = {"name": "Планшет", "price": 300.00, "quantity": 3}

    product = Product.new_product(product_data)

    assert isinstance(product, Product)
    assert product.name == "Планшет"
    assert product.price == 300.00
    assert product.quantity == 3
