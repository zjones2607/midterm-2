class Supplier:
    def __init__(self, name): self.name = name
    def __str__(self): return self.name

class Product:
    def __init__(self, name, price, supplier, qty=0):
        self.name, self.price, self.supplier, self.qty = name, price, supplier, qty
    def restock(self, amt): self.qty += amt
    def __str__(self): return f"{self.name} (${self.price}) Qty:{self.qty} Supplier:{self.supplier}"

class Inventory:
    def __init__(self): self.products = []
    def add(self, p): self.products.append(p)
    def restock(self, name, amt):
        for p in self.products:
            if p.name == name:
                p.restock(amt)
                break
    def print_all(self):
        for p in self.products: print(p)

s1 = Supplier("Acme")
s2 = Supplier("Globex")
i = Inventory()
i.add(Product("Widget", 10.99, s1, 15))
i.add(Product("Gadget", 23.5, s2, 5))
i.print_all()
i.restock("Widget", 10)
print("\nAfter restock:")
i.print_all()