# Basic Programs using Dictionaries in Python

# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

# Create a dictionary with Hindi words and their English translations
hindi_to_english = {
    "नमस्ते": "Hello",
    "धन्यवाद": "Thank you",
    "कृपया": "Please",
    "शुभकामनाएँ": "Best wishes",
    "सुप्रभात": "Good morning",
    "शुभ रात्रि": "Good night"
}
# Function to look up a Hindi word
def lookup_word(hindi_word):
    return hindi_to_english.get(hindi_word, "Word not found in dictionary.")
# Main program loop
def main():
    print("Welcome to the Hindi-English Dictionary!")
    while True:
        print("\nEnter a Hindi word to look up its English translation (or type 'exit' to quit):")
        user_input = input("Hindi Word: ")
        
        if user_input.lower() == 'exit':
            print("Exiting the dictionary. Goodbye!")
            break
        
        translation = lookup_word(user_input)
        print(f"English Translation: {translation}")

if __name__ == "__main__":
    main()
# This program allows users to look up Hindi words and get their English translations.
# It continues to prompt for input until the user decides to exit.
# The dictionary can be easily expanded with more words as needed.

# Can we have a set with 18 (int) and '18' (str) as a value in it?
# No, a set cannot have both an integer and a string with the same value as separate elements.
# A set is a collection of unique elements, and in Python, the integer 18 and the string '18' are considered different types.
# However, you can have both in a set, but they will be treated as distinct elements.
# Example:
example_set = {18, '18'}
print("Example Set:", example_set)
# This example set contains both the integer 18 and the string '18' as distinct elements.

"""
What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?"""

s = set()
s.add(20)
s.add(20.0)
s.add('20')
print("Length of set s after adding elements:", len(s))
# The length of the set s after these operations will be 2.
# This is because 20 and 20.0 are considered the same value (both represent the integer 20),
# so they are treated as a single element in the set. The string '20' is treated as a distinct element.
# Therefore, the set will contain two unique elements: {20, '20'}.

# Pls determine the type of s in the below code snippet:
s = {}
print("Type of s:", type(s))
# The type of s in the code snippet is <class 'dict'>.
# This is because the curly braces {} are used to create an empty dictionary in Python.
# If you want to create an empty set, you should use the set() constructor instead.

# What will happen if we make a dictonary with a duplicate key?
# If you create a dictionary with a duplicate key, the last value assigned to that key will overwrite any previous values.
# For example:
duplicate_dict = {
    'key1': 'value1',
    'key2': 'value2',
    'key1': 'new_value1'  # This will overwrite the previous value for 'key1'
}
print("Dictionary with duplicate key:", duplicate_dict)
# The output will be: {'key1': 'new_value1', 'key2': 'value2'}
# This shows that the value for 'key1' has been updated to 'new_value1', and the previous value 'value1' is lost.


"""
Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}"""
# No, you cannot change the values inside a list that is contained in a set.
# This is because sets in Python are designed to hold immutable (unchangeable) elements.
# Lists are mutable, meaning you can change their contents, but they cannot be directly added to a set.
# If you try to add a list to a set, it will raise a TypeError.