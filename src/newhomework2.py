from abc import ABC, abstractmethod

class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

class Product(BaseProduct):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name=name, price=price, quantity=quantity)

    def get_info(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):
    def __init__(self, name: str, price: float, quantity: int, brand: str):
        super().__init__(name, price, quantity)
        self.brand = brand


print(Smartphone.mro)
g= Product("htf",500,7)
print(g)