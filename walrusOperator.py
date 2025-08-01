# Walrus Operator in Python
# This code demonstrates the use of the walrus operator (:=) introduced in Python 3.8.
# The walrus operator allows assignment within an expression.
# Example of using the walrus operator to assign a value while checking a condition
def process_data(data):
    # Using the walrus operator to assign and check the length of data
    if (n := len(data)) > 0:
        print(f"Processing {n} items.")
        for item in data:
            print(f"Item: {item}")
    else:
        print("No items to process.")
# Example usage
if __name__ == "__main__":
    sample_data = [1, 2, 3, 4, 5]
    process_data(sample_data)
    
    empty_data = []
    process_data(empty_data)
# This code will print the number of items being processed and each item in the list.
# If the list is empty, it will indicate that there are no items to process.
# The walrus operator is particularly useful for reducing redundancy in code.
# It allows for cleaner and more concise code by combining assignment and condition checking.
# The example demonstrates how to use the walrus operator effectively in a function.
# The walrus operator can also be used in list comprehensions and other expressions.
# The walrus operator is a powerful feature that can enhance code readability and efficiency.
# The walrus operator is also known as the assignment expression operator.
# It is useful in various scenarios where you want to avoid multiple evaluations of the same expression.
# The walrus operator can be used in loops, comprehensions, and conditional statements.
