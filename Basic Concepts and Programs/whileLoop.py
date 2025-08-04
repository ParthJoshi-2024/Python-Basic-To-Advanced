# While loops in Python
# This program demonstrates the use of while loops in Python.
# Key Features of While Loops:
# 1. Repeats a block of code as long as a condition is true.
# 2. Useful for scenarios where the number of iterations is not known beforehand.
# 3. Can be used for input validation or repeated tasks until a condition is met.
# Example of a simple while loop
def simple_while_loop():
    count = 0
    while count < 5:
        print("Count is:", count)
        count += 1
# Main program loop
def main():
    print("Welcome to the Simple While Loop Program!")
    while True:
        user_input = input("\nType 'run' to execute the loop or 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        elif user_input.lower() == 'run':
            simple_while_loop()
        else:
            print("Invalid input. Please type 'run' or 'exit'.")

# Main function to run the program
if __name__ == "__main__":
    main()

# While loops in Sets, Lists, and Dictionaries

# While loop in Sets
def while_loop_in_set():
    my_set = {1, 2, 3, 4, 5}
    iterator = iter(my_set)
    while True:
        try:
            item = next(iterator)
            print("Set item:", item)
        except StopIteration:
            break

# Explainin the above code
# The above code demonstrates how to iterate through a set using a while loop.
# It uses an iterator to access each item in the set until all items have been processed.
# iter() creates an iterator for the set, and next() retrieves the next item.

# While loop in Lists
def while_loop_in_list():
    my_list = [10, 20, 30, 40, 50]
    index = 0
    while index < len(my_list):
        print("List item:", my_list[index])
        index += 1

# Explaining the above code
# The above code demonstrates how to iterate through a list using a while loop.
# It uses an index to access each item in the list until all items have been processed.

# While loop in Dictionaries
def while_loop_in_dict():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    keys = list(my_dict.keys())
    index = 0
    while index < len(keys):
        key = keys[index]
        print(f"Dictionary item: {key} -> {my_dict[key]}")
        index += 1
# Explaining the above code
# The above code demonstrates how to iterate through a dictionary using a while loop.
# It converts the dictionary keys to a list and uses an index to access each key-value pair.