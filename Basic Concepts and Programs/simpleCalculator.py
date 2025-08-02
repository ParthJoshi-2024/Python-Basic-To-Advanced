# Simple Calculator Program

def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operation == 'average':
        return (num1 + num2) / 2
    else:
        return "Error: Invalid operation."

if __name__ == "__main__":
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()

        result = calculate(num1, num2, operation)
        print(f"The result of {operation}ing {num1} and {num2} is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")

# Note: This program performs basic arithmetic operations and handles division by zero.
# It also includes error handling for invalid inputs.

