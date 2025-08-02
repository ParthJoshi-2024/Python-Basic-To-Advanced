# Dunder methods in Python
# Dunder methods, or magic methods, are special methods in Python that start and end with double underscores. They allow you to define the behavior of your objects for built-in operations.
# Common dunder methods include __init__ for object initialization, __str__ for string representation, and __add__ for addition operations.
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass with value: {self.value}"

    def __add__(self, other):
        if isinstance(other, MyClass):
            return MyClass(self.value + other.value)
        return NotImplemented
    
# Example usage of dunder methods
obj1 = MyClass(10)
obj2 = MyClass(20)
print(obj1)  # Output: MyClass with value: 10
print(obj2)  # Output: MyClass with value: 20
print(obj1 + obj2)  # Output: MyClass with value: 30
print(obj1.__str__())  # Output: MyClass with value: 10
print(obj1.__add__(obj2))  # Output: MyClass with value: 30
print(obj1 + 5)  # Output: NotImplemented, since 5 is not an instance of MyClass
print(obj1 + "test")  # Output: NotImplemented, since "test" is not an instance of MyClass
