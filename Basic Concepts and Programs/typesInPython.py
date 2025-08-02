# Datatypes and Type Casting in Python
# Python has several built-in data types that are used to store values.
# 1. Integer - int
# 2. Floating Point - float
# 3. String - str
# 4. Boolean - bool
# 5. List - list
# 6. Tuple - tuple
# 7. Dictionary - dict
# 8. Set - set
# 9. NoneType - None

# Example of each data type
integer_value = 42
float_value = 3.14
string_value = "Hello, World!"
boolean_value = True
list_value = [1, 2, 3, 4, 5]
tuple_value = (1, 2, 3)
dictionary_value = {"key1": "value1", "key2": "value2"}
set_value = {1, 2, 3, 4, 5}
none_value = None
print("Data Types in Python:")
print(f"Integer: {integer_value} (Type: {type(integer_value)})")
print(f"Float: {float_value} (Type: {type(float_value)})")
print(f"String: '{string_value}' (Type: {type(string_value)})")
print(f"Boolean: {boolean_value} (Type: {type(boolean_value)})")
print(f"List: {list_value} (Type: {type(list_value)})")
print(f"Tuple: {tuple_value} (Type: {type(tuple_value)})")
print(f"Dictionary: {dictionary_value} (Type: {type(dictionary_value)})")
print(f"Set: {set_value} (Type: {type(set_value)})")
print(f"NoneType: {none_value} (Type: {type(none_value)})")


# Type Casting in Python
# Type casting is the process of converting one data type to another.
# Example of type casting
int_value = int(float_value)  # Converting float to int
str_value = str(integer_value)  # Converting int to str
print("Type Casting in Python:")
print(f"Converted Float to Int: {int_value} (Type: {type(int_value)})")
print(f"Converted Int to String: '{str_value}' (Type: {type(str_value)})")
