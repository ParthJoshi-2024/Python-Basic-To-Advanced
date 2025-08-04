# If, Elif and Else Statements in Python
# This program demonstrates the use of if, elif, and else statements in Python.
# Example of if, elif, and else statements
# Function to check the number and print a message
def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."

# Main program loop
def main():
    print("Welcome to the Number Checker!")
    while True:
        try:
            user_input = input("\nEnter a number to check (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break
            
            number = float(user_input)
            result = check_number(number)
            print(result)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Write a program to print yes when the age entered by the user is greater than or equal to 18.
def check_age(age):
    if age >= 18:
        return "Yes"
    else:
        return "No"
def main_age():
    print("Welcome to the Age Checker!")
    while True:
        try:
            user_input = input("\nEnter your age (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break
            
            age = int(user_input)
            result = check_age(age)
            print(result)
        except ValueError:
            print("Invalid input. Please enter a valid age.")

