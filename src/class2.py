class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Количество товара не может быть нулевым.")
        self.name = name
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для получения цены продукта."""
        return self.__price

    def __str__(self):
        return f"{self.name}, {self.price} руб остаток: {self.quantity}"

    def __add__(self, other):
        if isinstance(other, Product):
            total_price = (self.price * self.quantity) + (other.price * other.quantity)
            total_quantity = self.quantity + other.quantity
            # Создаем новый объект Product с суммарной стоимостью и количеством
            return Product(
                "Суммарный товар",
                total_price / total_quantity if total_quantity > 0 else 0,
                total_quantity,
            )
        return NotImplemented

    @price.setter
    def price(self, value: float):
        """Сеттер для установки цены продукта."""
        if value < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self.__price = value

    def __repr__(self):
        return (
            f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"
        )

    @classmethod
    def new_product(cls, product_info: dict):
        """Создает новый объект Product из словаря с информацией о товаре."""
        name = product_info.get("name")
        price = product_info.get("price")
        quantity = product_info.get("quantity")

        if name is None or price is None or quantity is None:
            raise ValueError(
                "Все параметры (name, price, quantity) должны быть указаны."
            )

        if quantity == 0:
            raise ValueError("Количество товара не может быть нулевым.")

        return cls(name, price, quantity)


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []  # Приватный атрибут для хранения списка товаров
        Category.total_categories += 1

    def average_price(self):
        if not self.products:
            return 0  # Если товаров нет, возвращаем 0

        total_price = sum(product.price for product in self.products)
        total_quantity = sum(product.quantity for product in self.products)

        try:
            average = total_price / total_quantity
        except ZeroDivisionError:
            return 0  # Если сумма товаров равна 0, возвращаем 0

        return average

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.description}"

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.products.append(product)  # Добавляем продукт в список
            Category.total_products += 1  # Увеличиваем общее количество товаров
        else:
            raise ValueError("Только объекты класса Product могут быть добавлены.")

    def get_products(self):
        return self.products[:]  # Возвращаем копию списка товаров для чтения

    def list_products(self):
        """Возвращает список товаров в формате: Название продукта, цена руб. Остаток: количество шт."""
        return [
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.products
        ]

    def __repr__(self):
        return (
            f"Category(name={self.name}, description={self.description}, "
            f"total products={len(self.products)})"
        )


product_data = {"name": "Смартфон", "price": 500.00, "quantity": 5}

# Создаем новый продукт с помощью класса-метода
new_product = Product.new_product(product_data)

# Создаем категорию и добавляем продукт
electronics_category = Category("Электроника", "Устройства и гаджеты")
electronics_category.add_product(new_product)

# Вывод информации о категории с товарами
print(electronics_category)  # Вывод информации о категории
print(electronics_category.list_products())
