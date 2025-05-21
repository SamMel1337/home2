from src.class2 import Category, Product
from src.exceptions import Exception_Value
from src.Inheritance2 import Smartphone

if __name__ == "__main__":

    product_data = {"name": "Смартфон", "price": 500.00, "quantity": 5}

    # Создаем новый продукт с помощью класса-метода
    new_product = Product.new_product(product_data)

    # Создаем категорию и добавляем продукт
    electronics_category = Category("Электроника", "Устройства и гаджеты")
    electronics_category.add_product(new_product)

    # Вывод информации о категории с товарами
    print(electronics_category)  # Вывод информации о категории
    print(electronics_category.list_products())

    try:
        product = Exception_Value("dd", 0, 0)
    except ValueError as e:
        print(e)

product_data3 = {"name": "Смартфон", "price": 500.00, "quantity": 5}
product_data1 = {"name": "Смартфон", "price": 500.00, "quantity": 5}

product1 = Product.new_product(product_data1)

product_data2 = {"name": "Планшет", "price": 300.00, "quantity": 3}
product2 = Product.new_product(product_data2)
"""Создаем новый продукт с помощью класса-метода"""
new_product = Product.new_product(product_data3)

"""Вывод информации о категории с товарами"""
total_product = product1 + product2
print(total_product)

g = Product("htf", 500.0, 7)
print(g)

s = Smartphone("iPhone", 999.99, 3, "Apple")
print(s)
