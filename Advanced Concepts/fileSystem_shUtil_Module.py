# shUtil module for file system operations
# How to use the shUtil module for file system operations in Python.

import os
import shutil
shutil.rmtree('example_directory')  # Remove a directory and all its contents

# Copy files
shutil.copy('source.txt', 'destination.txt')  # Copy a file
shutil.copy2('source.txt', 'destination.txt')  # Copy a file with metadata

# Remove directories or files
def remove_directory(path):
    try:
        os.rmdir(path)
        return True
    except OSError as e:
        print(f"Error removing directory: {e}")
        return False
    
# Move files
def move_file(source, destination):
    try:
        shutil.move(source, destination)
        return True
    except OSError as e:
        print(f"Error moving file: {e}")
        return False
    
# Create Files and Directories
def create_file(file_path):
    try:
        with open(file_path, 'w') as f:
            f.write('')  # Create an empty file
        return True
    except OSError as e:
        print(f"Error creating file: {e}")
        return False
    
# Nested Directory Creation
def create_nested_directories(path):
    try:
        os.makedirs(path)
        return True
    except OSError as e:
        print(f"Error creating nested directories: {e}")
        return False
    
