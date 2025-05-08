import unittest
from src.newhomework2 import Product, Smartphone  # Замените your_module на имя вашего файла с классами

class TestProduct(unittest.TestCase):

    def setUp(self):
        """Создаем объекты для тестирования"""
        self.product = Product(name="Товар A", price=100.00, quantity=10)
        self.smartphone = Smartphone(name="Смартфон A", price=500.00, quantity=5, brand="BrandX")

    def test_product_initialization(self):
        """Тестируем инициализацию продукта"""
        self.assertEqual(self.product.name, "Товар A")
        self.assertEqual(self.product.price, 100.00)
        self.assertEqual(self.product.quantity, 10)

    def test_product_get_info(self):
        """Тестируем метод get_info"""
        expected_info = "Товар A, 100.0 руб. Остаток: 10 шт."
        self.assertEqual(self.product.get_info(), expected_info)

    def test_smartphone_initialization(self):
        """Тестируем инициализацию смартфона"""
        self.assertEqual(self.smartphone.name, "Смартфон A")
        self.assertEqual(self.smartphone.price, 500.00)
        self.assertEqual(self.smartphone.quantity, 5)
        self.assertEqual(self.smartphone.brand, "BrandX")

    def test_smartphone_get_info(self):
        """Тестируем метод get_info у смартфона"""
        expected_info = "Смартфон A, 500.0 руб. Остаток: 5 шт."
        self.assertEqual(self.smartphone.get_info(), expected_info)

if __name__ == '__main__':
    unittest.main()