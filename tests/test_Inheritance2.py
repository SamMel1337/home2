import pytest
from src.Inheritance2 import Product, Smartphone  # Убедитесь, что импорт корректен


@pytest.fixture
def setup_objects():
    """Создаем объекты для тестирования"""
    product = Product(name="Товар A", price=100.00, quantity=10)
    smartphone = Smartphone(name="Смартфон A", price=500.00, quantity=5, brand="BrandX")
    return product, smartphone


def test_product_initialization(setup_objects):
    product, _ = setup_objects
    assert product.name == "Товар A"
    assert product.price == 100.00
    assert product.quantity == 10


def test_product_get_info(setup_objects):
    product, _ = setup_objects
    expected_info = "Товар A, 100.0 руб. Остаток: 10 шт."
    assert product.get_info() == expected_info


def test_smartphone_initialization(setup_objects):
    _, smartphone = setup_objects
    assert smartphone.name == "Смартфон A"
    assert smartphone.price == 500.00
    assert smartphone.quantity == 5
    assert smartphone.brand == "BrandX"


def test_smartphone_get_info(setup_objects):
    _, smartphone = setup_objects
    expected_info = "Смартфон A, 500.0 руб. Остаток: 5 шт."
    assert smartphone.get_info() == expected_info
