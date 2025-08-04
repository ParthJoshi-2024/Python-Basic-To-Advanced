# Write a program to find the greatest of four numbers entered by the user.
# Function to find the greatest of four numbers
def find_greatest(num1, num2, num3, num4):
    greatest = num1  # Assume the first number is the greatest initially
    if num2 > greatest:
        greatest = num2
    if num3 > greatest:
        greatest = num3
    if num4 > greatest:
        greatest = num4
    return greatest

# Main program to get user input and find the greatest number
def main():
    print("Enter four numbers to find the greatest among them:")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter fourth number: "))
        
        greatest_number = find_greatest(num1, num2, num3, num4)
        print(f"The greatest number among the entered values is: {greatest_number}")
    except ValueError:
        print("Please enter valid numbers.")

