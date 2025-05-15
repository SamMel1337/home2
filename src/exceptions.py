class Exception_Value(Exception):
    def __init__(self, name, quantity, price):
        if price == 0:
            raise ValueError("Товар с нулевой ценой не может быть добавлен")
        self.name = name
        self.quantity = quantity
        self.price = price

try:
    product = Exception_Value("dd", 0, 0)
except ValueError as e:
    print(e)

