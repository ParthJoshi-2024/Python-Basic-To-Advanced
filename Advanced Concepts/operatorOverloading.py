# Operator Overloading in Python
# Operator overloading allows you to define the behavior of operators for user-defined classes.
# This enables you to use operators like +, -, *, etc., with your custom objects.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

# Example usage of operator overloading
v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)  # Output: Vector(6, 8)
print(v1 - v2)  # Output: Vector(-2, -2)
print(v1 * 3)   # Output: Vector(6, 9)
print(v1 == v2)  # Output: False
print(v1 == Vector(2, 3))  # Output: True
# The use of operator overloading allows for intuitive operations on custom objects, making the code more readable and expressive.
# In this example, the Vector class overloads the +, -, *, and == operators to perform vector addition, subtraction, scalar multiplication, and equality comparison, respectively.
# This allows instances of the Vector class to be used with these operators just like built-in types.
# Operator overloading is a powerful feature in Python that enhances the usability of custom classes by allowing them to behave like built-in types.
# This makes the code more intuitive and easier to read, as it allows for natural expressions involving custom objects.
# Operator overloading can be particularly useful in mathematical or geometric applications, where custom objects represent mathematical entities like vectors, matrices, or complex numbers.
# It also allows for cleaner and more expressive code, as you can use standard operators instead of method calls.
# However, it's important to use operator overloading judiciously, as it can lead to confusion if the overloaded operators do not behave in a way that is consistent with their usual meanings.
# In summary, operator overloading in Python allows you to define custom behavior for operators, making your classes more intuitive and expressive.