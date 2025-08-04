# Recursion in Python
# Key Features of Recursion:
# Recursion is a programming technique where a function calls itself to solve a problem.
# 1. It is often used to solve problems that can be broken down into smaller, similar subproblems.
# 2. Each recursive call should bring the problem closer to a base case, which stops the recursion.
# 3. It can lead to elegant solutions for problems like factorial calculation, Fibonacci sequence, and tree traversals.
# 4. Recursion can be less efficient than iterative solutions due to function call overhead and stack depth limitations.
# 5. Python has a recursion limit (default is 1000), which can be adjusted using sys.setrecursionlimit().
# 6. Recursive functions should always have a base case to prevent infinite recursion.
# 7. Recursive solutions can be more readable and easier to understand for certain problems.
# 8. It can lead to stack overflow errors if the recursion depth exceeds the limit.
# 9. Tail recursion optimization is not supported in Python, meaning that recursive calls do not reuse the stack frame.
# 10. Recursion can be used in algorithms like quicksort, mergesort, and depth-first search.
# 11. Recursive functions can be more challenging to debug due to multiple function calls and stack traces.
# 12. It is important to ensure that the recursive function has a clear exit condition to avoid infinite loops.

def factorial(n):
    """Calculate factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def fibonacci(n):
    """Calculate nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Main function to run the recursion examples
def main():
    print("Welcome to the Recursion Program!")
    while True:
        user_input = input("\nType 'factorial' to calculate factorial, 'fibonacci' for Fibonacci sequence, or 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        elif user_input.lower() == 'factorial':
            num = int(input("Enter a number to calculate its factorial: "))
            print(f"Factorial of {num} is: {factorial(num)}")
        elif user_input.lower() == 'fibonacci':
            num = int(input("Enter a position in the Fibonacci sequence: "))
            print(f"The {num}th Fibonacci number is: {fibonacci(num)}")
        else:
            print("Invalid input. Please type 'factorial', 'fibonacci', or 'exit'.")


