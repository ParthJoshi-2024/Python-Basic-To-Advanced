# Tuples in Python
# A tuple is a collection of items that can be of different types.
# Tuples are immutable, meaning you cannot change their content after creation.

# Creating a tuple
my_tuple = (1, 2, 3, 'apple', 'banana')
# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1

# Finding the length of a tuple: You can find the number of elements in a tuple using len().
print(len(my_tuple))  # Output: 5

# Checking if an item exists in a tuple: You can check if an item is in a tuple using the 'in' keyword.
if 'apple' in my_tuple:
    print("'apple' is in the tuple")  # Output: 'apple' is in the tuple

# Iterating through a tuple: You can loop through the elements of a tuple using a for loop.
for item in my_tuple:
    print(item)  # Prints each item in the tuple

# Slicing a tuple: You can access a range of elements in a tuple using slicing.
sliced_tuple = my_tuple[1:4]
print(sliced_tuple)  # Output: (2, 3, 'apple')

# Concatenating tuples: You can combine two or more tuples using the + operator.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Finding the index of an item in a tuple: You can find the first occurrence of an item using index().
index_of_apple = my_tuple.index('apple')
print(index_of_apple)  # Output: 3

# Counting occurrences of an item in a tuple: You can count how many times an item appears using count().
count_of_1 = my_tuple.count(1)
print(count_of_1)  # Output: 1

# Unpacking a tuple: You can assign the elements of a tuple to multiple variables.
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # Output: 1 2 3 apple banana

# Nested tuples: You can have tuples within tuples.
nested_tuple = (1, (2, 3), 'apple')
print(nested_tuple)  # Output: (1, (2, 3), 'apple')

# Using tuples as dictionary keys: Tuples can be used as keys in dictionaries since they are immutable.
my_dict = {my_tuple: "This is a tuple"}
print(my_dict[my_tuple])  # Output: This is a tuple
print(my_dict)  # Output: {(1, 2, 3, 'apple', 'banana'): 'This is a tuple'}

# Converting a tuple to a list: You can convert a tuple to a list using the list() function.
tuple_to_list = list(my_tuple)
print(tuple_to_list)  # Output: [1, 2, 3, 'apple', 'banana']

# Converting a list to a tuple: You can convert a list to a tuple using the tuple() function.
list_to_tuple = tuple(tuple_to_list)   
print(list_to_tuple)  # Output: (1, 2, 3, 'apple', 'banana')

# Using named tuples for better readability: Named tuples allow you to access elements by name instead of index.
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
point = Point(10, 20)
print(point.x, point.y)  # Output: 10 20

# Using tuples for fixed collections: Tuples are often used to represent fixed collections of items, such as coordinates or RGB values.
rgb = (255, 0, 0)  # Red color in RGB

# Using tuples for function return values: Functions can return multiple values as a tuple.
def get_coordinates():
    return (10, 20)
x, y = get_coordinates()
print(x, y)  # Output: 10 20

# Using tuples for data integrity: Since tuples are immutable, they can be used to ensure that the data remains unchanged throughout the program.
# This is particularly useful when passing data between functions or modules.
# Using tuples for performance: Tuples can be more memory-efficient than lists, especially for large collections of items.
# This can lead to performance improvements in certain scenarios.
