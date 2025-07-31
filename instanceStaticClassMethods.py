# Instance, Static, and Class Methods in Python
class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @staticmethod
    def static_method():
        return "This is a static method."

    @classmethod
    def class_method(cls):
        return f"This is a class method. Class variable: {cls.class_variable}"

    def instance_method(self):
        return f"This is an instance method. Instance variable: {self.instance_variable}"

# Lets see the use cases
instanceMethod = MyClass("I am an instance variable").instance_method()
print(instanceMethod)  # Output: This is an instance method. Instance variable: I am an instance variable

staticMethod = MyClass.static_method()
print(staticMethod)  # Output: This is a static method.

classMethod = MyClass.class_method()
print(classMethod)  # Output: This is a class method. Class variable: I am a class variable

# Difference between instance, static, and class methods
print("\nDifferences:")
print("Instance Method: Requires an instance of the class to be called.")
print("Static Method: Does not require an instance or class reference; can be called on the class itself.")
print("Class Method: Requires a class reference; can access class variables and methods.")
print("Instance methods can access instance variables, while class methods can access class variables.")
# Example of using the methods
instance = MyClass("Example Instance")
print(instance.instance_method())  # Output: This is an instance method. Instance variable: Example Instance
print(MyClass.static_method())  # Output: This is a static method.
print(MyClass.class_method())  # Output: This is a class method. Class variable: I am a class variable