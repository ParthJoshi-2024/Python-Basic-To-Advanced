# Dictionary in Python
# A dictionary is a collection of key-value pairs, where each key is unique.
# Importantly, dictionaries are mutable, meaning you can change their content after creation.

# Key concepts of dictionaries:
# 1. Keys must be immutable types (like strings, numbers, or tuples).
# 2. Values can be of any type and can be duplicated.

# Creating a dictionary
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Accessing values in a dictionary using keys
print(my_dict['name'])  # Output: Alice

# Adding a new key-value pair to a dictionary
my_dict['job'] = 'Engineer'
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

# Removing a key-value pair from a dictionary using del
del my_dict['age']
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York', 'job': 'Engineer'}

# Checking if a key exists in a dictionary
if 'city' in my_dict:
    print("City exists in the dictionary")  # Output: City exists in the dictionary

# Iterating through a dictionary: You can loop through keys, values, or both.
for key in my_dict:
    print(key, my_dict[key])  # Prints each key and its corresponding value
for key, value in my_dict.items():
    print(key, value)  # Prints each key and its corresponding value

# Getting the keys and values of a dictionary
keys = my_dict.keys()
values = my_dict.values()
print(keys)   # Output: dict_keys(['name', 'city', 'job'])
print(values) # Output: dict_values(['Alice', 'New York', 'Engineer'])

# Finding the length of a dictionary: You can find the number of key-value pairs using len().
print(len(my_dict))  # Output: 3

# Copying a dictionary: You can create a shallow copy of a dictionary using the copy() method.
# This is useful to avoid modifying the original dictionary.
copied_dict = my_dict.copy()
print(copied_dict)  # Output: {'name': 'Alice', 'city': 'New York', 'job': 'Engineer'}

# Merging dictionaries: You can merge two dictionaries using the update() method or the | operator in Python 3.9+.
another_dict = {'country': 'USA', 'hobby': 'Reading'}
my_dict.update(another_dict)
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York', 'job': 'Engineer', 'country': 'USA', 'hobby': 'Reading'}
# Using the | operator (Python 3.9+)
my_dict = my_dict | another_dict
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York', 'job': 'Engineer', 'country': 'USA', 'hobby': 'Reading'}

# Nested dictionaries: You can have dictionaries within dictionaries.
nested_dict = {
    'person': {
        'name': 'Bob',
        'age': 25
    },
    'location': {
        'city': 'Los Angeles',
        'state': 'California'
    }
}
print(nested_dict)  # Output: {'person': {'name': 'Bob', 'age': 25}, 'location': {'city': 'Los Angeles', 'state': 'California'}}

# Accessing nested dictionary values
print(nested_dict['person']['name'])  # Output: Bob

# Using dictionaries as sets: You can use dictionaries to store unique items by using the keys.
unique_items = {1: None, 2: None, 3: None}
print(unique_items)  # Output: {1: None, 2: None, 3: None}

# Converting a dictionary to a list of tuples: You can convert a dictionary to a list of key-value pairs.
dict_items = list(my_dict.items())
print(dict_items)  # Output: [('name', 'Alice'), ('city', 'New York'), ('job', 'Engineer'), ('country', 'USA'), ('hobby', 'Reading')]

# Converting a list of tuples to a dictionary: You can convert a list of key-value pairs back to a dictionary.
list_of_tuples = [('key1', 'value1'), ('key2', 'value2')]
converted_dict = dict(list_of_tuples)
print(converted_dict)  # Output: {'key1': 'value1', 'key2': 'value2'}

# Using default values with get(): You can retrieve a value for a key, and specify a default if the key does not exist.
value = my_dict.get('nonexistent_key', 'default_value')
print(value)  # Output: default_value

# Using dictionary comprehensions: You can create dictionaries using a concise syntax.
squared_numbers = {x: x**2 for x in range(5)}
print(squared_numbers)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}



