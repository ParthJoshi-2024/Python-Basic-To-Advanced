# For loops in Python
# Key Features of For Loops:
# 1. Iterates over a sequence (like a list, tuple, or string) or other iterable objects.
# 2. Automatically handles the iteration process, making it simpler than while loops for many use cases.
# 3. Useful for iterating through collections without needing to manage an index.
# 4. Can be used with the range() function to generate a sequence of numbers.

# Example of a simple for loop
def simple_for_loop():
    for i in range(5):
        print("Count is:", i)
def main():
    print("Welcome to the Simple For Loop Program!")
    while True:
        user_input = input("\nType 'run' to execute the loop or 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        elif user_input.lower() == 'run':
            simple_for_loop()
        else:
            print("Invalid input. Please type 'run' or 'exit'.")

# Range function in For Loops
def for_loop_with_range():
    for i in range(1, 11):
        print("Number:", i)
# Main function to run the program
if __name__ == "__main__":
    main()

# All paramters of the range function
def range_parameters():
    print("Range with one parameter:")
    for i in range(5):  # This will generate numbers from 0 to 4
        print(i)
    
    print("\nRange with two parameters:")
    for i in range(2, 8): # This will generate numbers from 2 to 7
        print(i)
    
    print("\nRange with three parameters:")
    for i in range(1, 10, 2): # This will generate numbers from 1 to 9 with a step of 2
        print(i)

# For loop with else
# Key Features of For Loop with Else:
# 1. The else block executes after the for loop completes normally (not interrupted by a break).
# 2. Useful for scenarios where you want to perform an action after iterating through all items.
# 3. The else block does not execute if the loop is exited prematurely with a break statement.
# 4. If the loop breaks out due to any exception or break statement, the else block will not execute.
def for_loop_with_else():
    for i in range(3):
        print("Iteration:", i)
    else:
        print("For loop completed without interruption.")

# Break statement in For Loops
# Key Features of Break Statement:
# 1. Exits the loop immediately when encountered.
# 2. Useful for stopping the loop based on a condition.
# 3. Can be used to exit nested loops.
def for_loop_with_break():
    for i in range(5):
        if i == 3:
            print("Breaking the loop at i =", i)
            break
        print("Current value of i:", i)

# Continue statement in For Loops
# Key Features of Continue Statement:
# 1. Skips the current iteration and continues with the next iteration of the loop.
# 2. Useful for skipping specific conditions without exiting the loop.
# 3. Can be used to skip processing certain items based on a condition.
def for_loop_with_continue():
    for i in range(5):
        if i == 2:
            print("Skipping the iteration at i =", i)
            continue
        print("Current value of i:", i)



