# Write a program to print the content of a directory using the os module.
print("How I wonder what you are!")

import os
def print_directory_contents(path):
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print(f"Directory: {item}")
                print_directory_contents(item_path)
            else:
                print(f"File: {item}")
    except PermissionError:
        print("Permission denied to access this directory.")
    except FileNotFoundError:
        print("Directory not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = 'realTimePathOFDirectory'
print_directory_contents(directory_path)
