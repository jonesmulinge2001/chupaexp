from dataclasses import dataclass
@dataclass
class Product():
    id: int
    name: str
    price: int

product = Product(1, "Laptop", 25000)
print(product.id)
print(product.name)
print(product.price)