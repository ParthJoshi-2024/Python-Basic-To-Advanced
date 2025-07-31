# Decorators in Python are a powerful tool that allows you to modify the behavior of a function or class method.
# They are often used for logging, access control, memoization, and other cross-cutting concerns.
# Decorator is a function that takes a function as an argument and returns a new function that adds some kind of functionality to the original function.

def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

f = decorator(say_hello)
f()
# Alternatively, you can use the `@decorator` syntax to apply the decorator to a function.
@decorator
def say_goodbye():
    print("Goodbye!")
say_goodbye()

