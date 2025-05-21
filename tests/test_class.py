import unittest


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

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Invalid product")
        self.products.append(product)


class TestProductAndCategory(unittest.TestCase):

    def setUp(self):
        """Set up test variables."""
        self.product1 = Product("Laptop", "A high-performance laptop", 1200.99, 10)
        self.product2 = Product("Smartphone", "A latest model smartphone", 799.99, 25)
        self.category = Category("Electronics", "Devices and gadgets")

    def test_product_creation(self):
        """Test if a Product is created correctly."""
        self.assertEqual(self.product1.name, "Laptop")
        self.assertEqual(self.product1.description, "A high-performance laptop")
        self.assertEqual(self.product1.price, 1200.99)
        self.assertEqual(self.product1.quantity, 10)

    def test_category_creation(self):
        """Test if a Category is created correctly."""
        self.assertEqual(self.category.name, "Electronics")
        self.assertEqual(self.category.description, "Devices and gadgets")
        self.assertEqual(len(self.category.products), 0)

    def test_add_product(self):
        """Test adding a product to a category."""
        self.category.add_product(self.product1)
        self.assertEqual(len(self.category.products), 1)
        self.assertEqual(self.category.products[0], self.product1)

    def test_add_multiple_products(self):
        """Test adding multiple products to a category."""
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        self.assertEqual(len(self.category.products), 2)
        self.assertIn(self.product1, self.category.products)
        self.assertIn(self.product2, self.category.products)

    def test_total_categories(self):
        """Test if the total categories count is correct."""
