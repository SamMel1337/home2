from abc import ABC, abstractmethod


class CreationLoggerMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Объект класса {self.__class__.__name__} был создан.")


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


class Product(CreationLoggerMixin, BaseProduct):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name=name, price=price, quantity=quantity)

    def get_info(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __str__(self):
        return self.get_info()


class Smartphone(Product):
    def __init__(self, name: str, price: float, quantity: int, brand: str):
        super().__init__(name=name, price=price, quantity=quantity)
        self.brand = brand

    def __str__(self):
        return f"{super().__str__()}, Бренд: {self.brand}"


# Проверка:
g = Product("htf", 500.0, 7)
print(g)

s = Smartphone("iPhone", 999.99, 3, "Apple")
print(s)
