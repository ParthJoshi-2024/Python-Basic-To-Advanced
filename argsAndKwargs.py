# Args and Kwargs in Python
# Args allows you to pass a variable number of positional arguments to a function.
# Args will be collected into a tuple.
# Kwargs will collect keyword arguments into a dictionary.

def print_args(*args):
    # Print each argument passed to the function
    for arg in args:
        print(f"Argument: {arg}")
# Example usage of print_args
print_args(1, 2, 3, "hello", [4, 5])

# Kwargs allows you to pass a variable number of keyword arguments to a function.
def print_kwargs(**kwargs):
    # Print each keyword argument passed to the function
    for key, value in kwargs.items():
        print(f"Keyword Argument: {key} = {value}")
# Example usage of print_kwargs
print_kwargs(name="Alice", age=30, city="New York")

# Combining *args and **kwargs in a single function
def print_args_and_kwargs(*args, **kwargs):
    # Print positional arguments
    print("Positional Arguments:")
    for arg in args:
        print(f"  {arg}")
    
    # Print keyword arguments
    print("Keyword Arguments:")
    for key, value in kwargs.items():
        print(f"  {key} = {value}")
# Example usage of print_args_and_kwargs
print_args_and_kwargs(1, 2, 3, name="Bob", age=25)
# This function demonstrates how to handle both positional and keyword arguments.
# It allows for flexible function calls and can be useful in various scenarios.
# The use of *args and **kwargs is common in Python for functions that need to handle a variable number of arguments.
# The combination of *args and **kwargs allows for versatile function definitions.
# The examples provided show how to use these features effectively in Python.
# The use of *args and **kwargs can simplify function definitions and make them more adaptable.
# Note: If you want to use both *args and **kwargs, *args must come before **kwargs in the function definition.