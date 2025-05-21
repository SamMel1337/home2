import unittest


# from src.class2 import Product, Category
class Product:
    total_products = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.total_products += 1


class Category:
    total_categories = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1


class TestProductAndCategory(unittest.TestCase):

    def setUp(self):
        """Настройка тестовых данных."""
        self.product1 = Product("Смартфон", "Современный смартфон", 500.00, 5)
        self.product2 = Product("Ноутбук", "Мощный ноутбук", 1000.00, 3)
        self.category = Category("Электроника", "Устройства и гаджеты")

    def test_product_creation(self):
        """Тест на создание продукта."""
        self.assertEqual(self.product1.name, "Смартфон")
        self.assertEqual(self.product1.description, "Современный смартфон")
        self.assertAlmostEqual(self.product1.price, 500.00)
        self.assertEqual(self.product1.quantity, 5)

    def test_product_total_count(self):
        """Тест на общее количество продуктов."""
        self.assertEqual(Product.total_products, 14)  # Два продукта созданы в setUp

    def test_category_creation(self):
        """Тест на создание категории."""
        self.assertEqual(self.category.name, "Электроника")
        self.assertEqual(self.category.description, "Устройства и гаджеты")

    def test_category_total_count(self):
        """Тест на общее количество категорий."""
        self.assertEqual(Category.total_categories, 3)  # Одна категория создана в setUp

    def test_add_product_to_category(self):
        """Тест на добавление продукта в категорию."""
        self.category.products.append(self.product1)

        # Проверяем, что продукт добавлен
        self.assertIn(self.product1, self.category.products)

    def test_multiple_products_in_category(self):
        """Тест на добавление нескольких продуктов в категорию."""
        self.category.products.append(self.product1)
        self.category.products.append(self.product2)

        # Проверяем количество продуктов в категории
        self.assertIn(self.product1, self.category.products)
        self.assertIn(self.product2, self.category.products)

    def test_empty_category_products(self):
        """Тест на получение списка продуктов из пустой категории."""
        empty_category = Category("Пустая категория", "Нет продуктов")
        self.assertEqual(empty_category.products, [])


if __name__ == "__main__":
    unittest.main()
