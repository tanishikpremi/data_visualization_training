# Q9. Develop a dictionary-based inventory management system where users can 
# add products, update quantity, search products, and display low-stock items.

class Inventory:
    def __init__(self): self.items = {}
    def add(self, pid, name, qty): self.items[pid] = {'name': name, 'qty': qty}
    def update(self, pid, qty): 
        if pid in self.items: self.items[pid]['qty'] = qty
    def search(self, pid): return self.items.get(pid, "Not found")
    def low_stock(self, limit=10):
        return {k: v for k, v in self.items.items() if v['qty'] < limit}

if __name__ == "__main__":
    inv = Inventory()
    inv.add("P1", "Laptop", 5)
    inv.add("P2", "Mouse", 15)
    inv.update("P1", 8)
    print(f"Search P1: {inv.search('P1')}")
    print(f"Low Stock: {inv.low_stock()}")

# Expected Output:
# Search P1: {'name': 'Laptop', 'qty': 8}
# Low Stock: {'P1': {'name': 'Laptop', 'qty': 8}}
