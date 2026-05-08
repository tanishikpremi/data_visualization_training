# self learning - OOP basics
# topic: classes, objects, inheritance
# honestly struggled with this at first, making notes to come back to

# ── class basics ───────────────────────────────

class Student:
    # class variable (shared by all instances)
    school = "Data Academy"

    def __init__(self, name, age, grade):
        # instance variables (unique to each object)
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old. Grade: {self.grade}"

    def is_passing(self):
        return self.grade >= 60

    # __str__ makes print() work nicely
    def __str__(self):
        return f"Student({self.name}, {self.age})"

    # __repr__ for debugging
    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, grade={self.grade})"


# creating objects
s1 = Student("Alice", 21, 88)
s2 = Student("Bob", 22, 55)

print(s1.introduce())
print(s2.is_passing())   # False
print(Student.school)    # Data Academy
print(s1)                # uses __str__
print(repr(s1))          # uses __repr__

# ── inheritance ────────────────────────────────
# child class gets all methods from parent
# and can add its own or override them

class GraduateStudent(Student):
    def __init__(self, name, age, grade, thesis_topic):
        super().__init__(name, age, grade)   # calling parent __init__
        self.thesis_topic = thesis_topic

    def introduce(self):
        # overriding the parent method
        base = super().introduce()
        return f"{base} | Thesis: {self.thesis_topic}"

    def thesis_summary(self):
        return f"{self.name} is working on: {self.thesis_topic}"


grad = GraduateStudent("Charlie", 25, 91, "Machine Learning in Healthcare")
print(grad.introduce())
print(grad.thesis_summary())
print(grad.school)   # still inherited from Student

# ── encapsulation - private variables ──────────
# convention: _ = protected, __ = private (name mangling)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance


acc = BankAccount("Tanishik", 5000)
acc.deposit(2000)
acc.withdraw(1000)
print("Balance:", acc.get_balance())
# print(acc.__balance)  # ❌ AttributeError - can't access directly (good!)

# TODO: learn about:
# - @property decorator
# - class methods (@classmethod)
# - static methods (@staticmethod)
# - multiple inheritance
