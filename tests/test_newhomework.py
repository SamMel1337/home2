import unittest
from src.class2 import Product  # Убедитесь, что этот импорт корректен
from src.newhomework import (
    Smartphone,
    LawnGrass,
)  # Замените your_module на имя вашего файла


class TestProduct(unittest.TestCase):

    def setUp(self):
        """Создаем объекты для тестирования"""
        self.smartphone1 = Smartphone(name="Смартфон A", price=500.00, quantity=5)
        self.smartphone2 = Smartphone(name="Смартфон B", price=500.00, quantity=5)
        self.lawn_grass = LawnGrass(name="Газонная трава", price=100.00, quantity=10)

    def test_smartphone_initialization(self):
        """Тестируем инициализацию смартфона"""
        self.assertEqual(self.smartphone1.name, "Смартфон A")
        self.assertEqual(self.smartphone1.price, 500.00)
        self.assertEqual(self.smartphone1.quantity, 5)

    def test_add_products_same_type(self):
        """Тестируем сложение продуктов одного типа"""
        total_product = self.smartphone1 + self.smartphone2
        self.assertEqual(total_product.name, "Суммарный товар")
        self.assertEqual(total_product.price, 500.00)  # Средняя цена
        self.assertEqual(total_product.quantity, 10)

    def test_add_products_different_type(self):
        """Тестируем сложение продуктов разных типов"""
        with self.assertRaises(TypeError):
            _ = self.smartphone1 + self.lawn_grass

    def test_add_invalid_product(self):
        """Тестируем добавление недопустимого продукта"""
        with self.assertRaises(TypeError):
            self.smartphone1.add_product("Некорректный продукт")

    def test_add_valid_product(self):
        """Тестируем добавление корректного продукта"""
        self.smartphone1.add_product(self.smartphone2)
        self.assertIn(self.smartphone2, self.smartphone1.products)

    def test_new_product_creation(self):
        """Тестируем создание нового продукта через класс-метод"""
        product_data = {"name": "Планшет", "price": 300.00, "quantity": 3}

        product = Product.new_product(product_data)

        self.assertIsInstance(product, Product)
        self.assertEqual(product.name, "Планшет")
        self.assertEqual(product.price, 300.00)
        self.assertEqual(product.quantity, 3)


if __name__ == "__main__":
    unittest.main()
