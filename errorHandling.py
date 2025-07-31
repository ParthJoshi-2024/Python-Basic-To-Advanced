# Error/ Exception Handling in Python
# Error handling in Python is done using try and except blocks. This allows you to catch and handle exceptions gracefully without crashing the program.
# You can also use else and finally blocks to execute code after the try block or clean up resources regardless of whether an exception occurred.
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError as e:
        print(f"Error: {e}. Cannot divide by zero.")
        return None
    except TypeError as e:
        print(f"Error: {e}. Please provide numbers.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    else:
        print("Division successful!")
        return result
    finally:
        print("Execution completed.")

# Example usage of error handling
result1 = divide_numbers(10, 2)
result2 = divide_numbers(10, 0)
result3 = divide_numbers(10, "a")
# result1 should print 5.0, result2 should handle division by zero, and result3 should handle type error.
# The finally block will always execute, regardless of whether an exception occurred or not.
# This example demonstrates how to handle different types of exceptions and ensure that cleanup code runs after the try-except block.
# Error handling is crucial for building robust applications that can handle unexpected situations gracefully.
# It allows developers to anticipate potential issues and provide meaningful feedback to users or log errors for debugging purposes.

# ------------------------------------------------------------------------------------------------------
# Rasing Exceptions
# You can also raise exceptions manually using the `raise` statement. This is useful when you want to enforce certain conditions in your code.
def check_positive_number(num):
    if num < 0:
        raise ValueError("The number must be positive.")
    return num
check_positive_number(10)  # This will return 10
# check_positive_number(-5)  # This will raise a ValueError with the message "The number must be positive."
