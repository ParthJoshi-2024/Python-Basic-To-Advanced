# Write a Python program to find the remainder when a number is divided by another number.
def find_remainder(dividend, divisor):
    try:
        remainder = dividend % divisor
        return remainder
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Please provide valid numbers."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    num1 = float(input("Enter the dividend: "))
    num2 = float(input("Enter the divisor: "))
    
    result = find_remainder(num1, num2)
    print(f"The remainder of {num1} divided by {num2} is: {result}")
