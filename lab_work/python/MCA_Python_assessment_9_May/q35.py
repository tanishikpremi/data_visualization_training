# Q35. Develop a contact management system using list and dictionary 
# where users can add, update, search, and delete contacts.

class ContactManager:
    def __init__(self): self.contacts = {}
    def add(self, name, phone): self.contacts[name] = phone
    def update(self, name, phone):
        if name in self.contacts: self.contacts[name] = phone
    def search(self, name): return self.contacts.get(name, "Not found")
    def delete(self, name):
        if name in self.contacts: del self.contacts[name]

if __name__ == "__main__":
    cm = ContactManager()
    cm.add("Alice", "1234567890")
    cm.add("Bob", "0987654321")
    print(f"Search Alice: {cm.search('Alice')}")
    cm.update("Alice", "1111111111")
    cm.delete("Bob")
    print(f"All contacts: {cm.contacts}")

# Expected Output:
# Search Alice: 1234567890
# All contacts: {'Alice': '1111111111'}
