# File System in Python
# How to read, write, and append files in Python.

# Opening a file for reading
f = open('example.txt', 'r')
content = f.read()
f.close() # Always close the file after reading

# Writing to a file
f = open('example.txt', 'w')  # 'w' mode will overwrite the file
f.write('Hello, World!\n')
f.close()  # Close the file after writing

# Note: If the file does not exist, it will be created in 'w' mode.
# If the file exists, it will be truncated to zero length. And the previous content will be lost. All the data will be overwritten from the new file. This only happens in 'w' mode.

# Appending to a file
f = open('example.txt', 'a')  # 'a' mode will append to the file
f.write('Appending a new line.\n')
f.close()  # Close the file after appending

# Append mode ('a') will not truncate the file. It will add new content at the end of the file without removing the existing content.



# If the file doesnot exists:
# 1. When the file is openened in 'r' mode, it will raise an error - FileNotFoundError.
# 2. When the file is opened in 'w' mode, it will create a new file.
# 3. When the file is opened in 'a' mode, it will also create a new file.


# Optimitzed way to read a file
with open('example.txt', 'r') as f:
    content = f.read() # Using 'with' statement ensures the file is closed automatically
# Writing to a file using 'with' statement
with open('example.txt', 'w') as f:
    f.write('Hello, World!\n')  # This will overwrite the file
# Appending to a file using 'with' statement
with open('example.txt', 'a') as f:
    f.write('Appending a new line.\n')  # This will append to the file
# The 'with' statement is preferred as it handles file closing automatically, even if an error occurs.
# Reading a file line by line
with open('example.txt', 'r') as f:
    for line in f:
        print(line.strip())  # Using strip() to remove any trailing newline characters
# Reading a file into a list of lines
with open('example.txt', 'r') as f: 
    lines = f.readlines()  # This reads all lines into a list
# Writing a list of lines to a file
with open('example.txt', 'w') as f:
    f.writelines(['First line.\n', 'Second line.\n', 'Third line.\n'])  # This writes multiple lines to the file
# Reading a file in binary mode
with open('example.txt', 'rb') as f:  # 'rb' mode for
    content = f.read()  # Reading the file in binary mode
# Writing to a file in binary mode
with open('example.txt', 'wb') as f:  # 'wb' mode for
    f.write(b'Hello, World!\n')  # Writing bytes to the file
# Appending to a file in binary mode
with open('example.txt', 'ab') as f:  # 'ab' mode for appending in binary
    f.write(b'Appending a new line in binary.\n')  # Appending bytes to the file
# Reading a file in text mode with encoding
with open('example.txt', 'r', encoding='utf-8') as f:  # Specify encoding
    content = f.read()  # Reading the file with specified encoding
# Writing to a file in text mode with encoding
with open('example.txt', 'w', encoding='utf-8') as f:  # Specify encoding
    f.write('Hello, World!\n')  # Writing text with specified encoding
# Appending to a file in text mode with encoding
with open('example.txt', 'a', encoding='utf-8') as f:  # Specify encoding
    f.write('Appending a new line with encoding.\n')  # Appending text with specified encoding
# Reading a file with error handling
try:
    with open('example.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")
    