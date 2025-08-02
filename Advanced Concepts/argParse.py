# Creating Command Line Utility with argparse
import argparse

parser = argparse.ArgumentParser(description="A simple command line utility.")

parser.add_argument('num1', type=float, help='First number for the operation')
parser.add_argument('num2', type=float, help='Second number for the operation')
parser.add_argument('operation', choices=["add", "sub", "mul", "div"], help='Operation to perform: add, sub, mul, or div')

args = parser.parse_args()

if(args.operation == "add"):
    result = args.num1 + args.num2
elif(args.operation == "sub"):
    result = args.num1 - args.num2
elif(args.operation == "mul"):
    result = args.num1 * args.num2
elif(args.operation == "div"):
    if args.num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit(1)
    result = args.num1 / args.num2
else:
    print("Invalid operation. Use add, sub, mul, or div.")
    exit(1)

if __name__ == "__main__":
    print(f"The result of {args.operation} operation on {args.num1} and {args.num2} is: {result}")

# Benifits of Command Line Utility:
# 1. Automation: Can be used in scripts or automated tasks.
# 2. Flexibility: Can be run with different parameters without changing the code.
# 3. Easy to use: Users can easily run the utility from the command line.
# 4. Reusability: Can be reused in different projects or scripts.
# 5. Integration: Can be integrated with other command line tools or scripts.