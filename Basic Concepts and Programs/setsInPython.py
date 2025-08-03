# Sets in Python
# A set is a collection of unique items that are unordered and unindexed.
# Sets are mutable, meaning you can change their content after creation.
# Key concepts of sets:
# 1. Sets do not allow duplicate items.
# 2. Sets are useful for membership testing and eliminating duplicate entries.
# 3. Sets are defined using curly braces or the set() function.
# 4. Sets do not support indexing, slicing, or other sequence-like behavior.


# Creating a set
my_set = {1, 2, 3, 'apple', 'banana'}

# Accessing elements in a set: You cannot access elements by index, but you can check for membership.
print('apple' in my_set)  # Output: True

# Adding an item to a set
my_set.add('orange')
print(my_set)  # Output: {1, 2, 3, 'apple', 'banana', 'orange'}

# Removing an item from a set using remove() or discard()
my_set.remove('banana')  # Raises KeyError if 'banana' is not found
print(my_set)  # Output: {1, 2, 3, 'apple', 'orange'}

my_set.discard('apple')  # Does not raise an error if 'apple' is not found
print(my_set)  # Output: {1, 2, 3, 'orange'}

# Clearing a set: You can remove all items from a set using clear().
my_set.clear()
print(my_set)  # Output: set()

# Checking if an item exists in a set
my_set = {1, 2, 3, 'apple', 'banana'}
if 'apple' in my_set:
    print("'apple' is in the set")  # Output: 'apple' is in the set

# Iterating through a set: You can loop through the elements of a set using a for loop.
for item in my_set:
    print(item)  # Prints each item in the set

# Finding the length of a set: You can find the number of unique items in a set using len().
print(len(my_set))  # Output: 5

# Copying a set: You can create a shallow copy of a set using the copy() method.
copied_set = my_set.copy()

print(copied_set)  # Output: {1, 2, 3, 'apple', 'banana'}

# Union of sets: You can combine two sets using the union() method or the | operator.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Using the | operator (Python 3.9+)
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection of sets: You can find common items in two sets using the intersection() method or the & operator.
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# Using the & operator (Python 3.9+)
intersection_set = set1 & set2
print(intersection_set)  # Output: {3}

# Difference of sets: You can find items that are in one set but not in another using the difference() method or the - operator.
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# Using the - operator (Python 3.9+)
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}

# Symmetric difference of sets: You can find items that are in either set but not in both using the symmetric_difference() method or the ^ operator.
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

# Using the ^ operator (Python 3.9+)
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

# Nested sets: You can have sets within sets, but the inner sets must be immutable (e.g., frozenset).
nested_set = {1, frozenset({2, 3}), 'apple'}
print(nested_set)  # Output: {1, frozenset({2, 3}), 'apple'}

# Using sets as dictionary keys: Sets cannot be used as dictionary keys since they are mutable, but frozensets can be used.
unique_items = {frozenset({1}), frozenset({2}), frozenset({3})}
print(unique_items)  # Output: {frozenset({1}), frozenset({2}), frozenset({3})}

# What is frozenset?
# A frozenset is an immutable version of a set. It can be used as a key in dictionaries or as an element in other sets.
my_frozenset = frozenset(my_set)
print(my_frozenset)  # Output: frozenset({1, 2, 3, 'apple', 'banana'})

# Converting a set to a list: You can convert a set to a list using the list() function.
set_to_list = list(my_set)
print(set_to_list)  # Output: [1, 2, 3, 'apple', 'banana']

# Converting a list to a set: You can convert a list to a set using the set() function.
list_to_set = set(set_to_list)
print(list_to_set)  # Output: {1, 2, 3, 'apple', 'banana'}

