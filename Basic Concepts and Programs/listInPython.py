# Lists in Python
# A list is a collection of items that can be of different types.
# Lists are mutable, meaning you can change their content.

# Creating a list
my_list = [1, 2, 3, 'apple', 'banana']

# Accessing elements in a list
print(my_list[0])  # Output: 1

# Sorting a list
new_list = [5, 2, 9, 1, 5, 6]
new_list.sort()
print(new_list)  # Output: [1, 2, 5, 5, 6, 9]

# Reversing a list
new_list.reverse()
print(new_list)  # Output: [9, 6, 5, 5, 2, 1]

# Appending elements to a list: New elements can be added to the end of a list using append().
new_list.append(10)
print(new_list)  # Output: [9, 6, 5, 5, 2, 1, 10]

# Inserting elements at a specific position: You can insert an element at a specific index using insert().
new_list.insert(2, 4) # Insert 4 at index 2
print(new_list)  # Output: [9, 6, 4, 5, 5, 2, 1, 10]

# Deleting elements from a list: You can remove elements using remove() or pop().
new_list.remove(5)  # Removes the first occurrence of 5
print(new_list)  # Output: [9, 6, 4, 5, 2, 1, 10]
new_list.pop()  # Removes the last element
print(new_list)  # Output: [9, 6, 4, 5, 2, 1]

# Finding the length of a list: You can find the number of elements in a list using len().
print(len(new_list))  # Output: 6

# Checking if an item exists in a list: You can check if an item is in a list using the 'in' keyword.
if 4 in new_list:
    print("4 is in the list")  # Output: 4 is in the list
    
# Iterating through a list: You can loop through the elements of a list using a for loop.
for item in new_list:
    print(item)  # Prints each item in the list