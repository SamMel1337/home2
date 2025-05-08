from src.class2 import Product


class Smartphone(Product):
    efficiency: str
    model: str
    memory: int
    color: str

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.products = []

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты одного класса Product.")

        if self.__class__ is not other.__class__:
            raise TypeError("Нельзя складывать продукты разных типов.")

        total_price = (self.price * self.quantity) + (other.price * other.quantity)
        total_quantity = self.quantity + other.quantity
        # Создаем новый объект Product с суммарной стоимостью и количеством
        return Product(
            "Суммарный товар",
            total_price / total_quantity if total_quantity > 0 else 0,
            total_quantity,
        )

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников."
            )

        self.products.append(product)


class LawnGrass(Product):
    country: str
    germination_period: int
    color: str

product_data = {
    'name': 'Смартфон',
    'price': 500.00,
    'quantity': 5
}
product_data1 = {
    'name': 'Смартфон',
    'price': 500.00,
    'quantity': 5
}

product1 = Product.new_product(product_data1)

product_data2 = {
    'name': 'Планшет',
    'price': 300.00,
    'quantity': 3
}
product2 = Product.new_product(product_data2)
"""Создаем новый продукт с помощью класса-метода"""
new_product = Product.new_product(product_data)

"""Вывод информации о категории с товарами"""
total_product = product1 + product2
print(total_product)