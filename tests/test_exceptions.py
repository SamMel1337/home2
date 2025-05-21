import pytest
from src.exceptions import Exception_Value  # Укажите правильный путь к вашему классу


def test_exception_value_zero_price():
    # Проверка, что при price=0 выбрасывается исключение
    with pytest.raises(ValueError) as exc_info:
        product = Exception_Value("dd", 0, 0)
    assert str(exc_info.value) == "Товар с нулевой ценой не может быть добавлен"


def test_exception_value_valid():
    # Проверка, что при корректных данных объект создается правильно
    product = Exception_Value("dd", 5, 10)
    assert product.name == "dd"
    assert product.quantity == 5
    assert product.price == 10
