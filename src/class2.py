class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

    @classmethod
    def new_product(cls, product_info: dict):
        """Создает новый объект Product из словаря с информацией о товаре."""
        name = product_info.get('name')
        price = product_info.get('price')
        quantity = product_info.get('quantity')

        if name is None or price is None or quantity is None:
            raise ValueError("Все параметры (name, price, quantity) должны быть указаны.")

        return cls(name, price, quantity)

class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут для хранения списка товаров

        Category.total_categories += 1

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)  # Добавляем продукт в список
            Category.total_products += 1  # Увеличиваем общее количество товаров
        else:
            raise ValueError("Только объекты класса Product могут быть добавлены.")

    def get_products(self):
        return self.__products[:]  # Возвращаем копию списка товаров для чтения

    def list_products(self):
        """Возвращает список товаров в формате: Название продукта, цена руб. Остаток: количество шт."""
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]

    def __repr__(self):
        return (f"Category(name={self.name}, description={self.description}, "
                f"total products={len(self.__products)})")

product_data = {
    'name': 'Смартфон',
    'price': 500.00,
    'quantity': 5
}

# Создаем новый продукт с помощью класса-метода
new_product = Product.new_product(product_data)

# Создаем категорию и добавляем продукт
electronics_category = Category("Электроника", "Устройства и гаджеты")
electronics_category.add_product(new_product)

# Вывод информации о категории с товарами
print(electronics_category)  # Вывод информации о категории
print(electronics_category.list_products())