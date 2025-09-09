from abc import ABC, abstractmethod
from datetime import date
from typing import List


class Item(ABC):
    @abstractmethod
    def get_discounted_price(self) -> float:
        pass

    @abstractmethod
    def export_data(self) -> dict:
        pass

class Book(Item):
    def __init__(self, title: str, price: float) -> None:
        self.title = title
        self.price = price

    def get_discounted_price(self):
        return self.price * 0.85
    
    def export_data(self):
        return { "title": self.title, "price": self.price}

class Food(Item):
    def __init__(self, name: str, expiry_date: date, price: float) -> None:
        self.name = name
        self.expiry_date = expiry_date
        self.price = price

    def get_discounted_price(self):
        return self.price

    def export_data(self):
        return { "name": self.name, "expiry_date": self.expiry_date, "price": self.price}
    

class Electronics(Item):
    def __init__(self, brand: str, price: float) -> None:
        self.brand = brand
        self.price = price

    def get_discounted_price(self):
        return self.price * 0.90
    
    def export_data(self):
        return { "brand": self.brand, "price": self.price}


items: List[Item] = [
    Book("Harry Potter", 20),
    Food("Milk", date.today(), 1.45),
    Electronics("Samsung", 150)
]

print("===DISCOUNTED PRICES===")
for item in items:
    discounted_price = item.get_discounted_price()
    print(f"discounted price: {discounted_price}")

print("===PRODUCTS EXPORT===")
for item in items:
    print(item.export_data())