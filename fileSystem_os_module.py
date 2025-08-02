# os module in Python for file system operations
# How to use the os module for file system operations in Python.
import os

# Check if a file exists
def file_exists(file_path):
    return os.path.isfile(file_path)

# Get the size of a file
def get_file_size(file_path):
    if file_exists(file_path):
        return os.path.getsize(file_path)
    else:
        return None
    
# Get the current working directory
def get_current_directory():
    return os.getcwd()

# Change the current working directory
def change_directory(path):
    try:
        os.chdir(path)
        return True
    except OSError as e:
        print(f"Error changing directory: {e}")
        return False
    
# List files in a directory
def list_files_in_directory(path='.'):
    try:
        return os.listdir(path)
    except OSError as e:
        print(f"Error listing files in directory: {e}")
        return []
    
# Create a new directory
def create_directory(path):
    try:
        os.makedirs(path)
        return True
    except OSError as e:
        print(f"Error creating directory: {e}")
        return False 
    
# Remove a file
def remove_file(file_path):
    try:
        os.remove(file_path)
        return True
    except OSError as e:
        print(f"Error removing file: {e}")
        return False

# Remove a directory
# Note: This will only remove empty directories. In order to remove a directory with files, use shutil.rmtree()
def remove_directory(path):
    try:
        os.rmdir(path)
        return True
    except OSError as e:
        print(f"Error removing directory: {e}")
        return False
    
# Rename a file or directory
def rename_file_or_directory(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        return True
    except OSError as e:
        print(f"Error renaming: {e}")
        return False
    
# Get absolute path of a file or directory
def get_absolute_path(path):
    return os.path.abspath(path)

# Check if a path is a directory
def is_directory(path):
    return os.path.isdir(path)

# Check if a path is a file
def is_file(path):
    return os.path.isfile(path)

# Get the last modified time of a file
def get_last_modified_time(file_path):
    if file_exists(file_path):
        return os.path.getmtime(file_path)
    else:
        return None
    

# Get the file extension
def get_file_extension(file_path):
    if file_exists(file_path):
        return os.path.splitext(file_path)[1]
    else:
        return None

# Get the base name of a file or directory
def get_base_name(path):
    return os.path.basename(path)

# Get the directory name of a file or directory
def get_directory_name(path):
    return os.path.dirname(path)

# Check if a path is absolute
def is_absolute_path(path):
    return os.path.isabs(path)

# Join two or more path components
def join_paths(*paths):
    return os.path.join(*paths)

# Get the environment variables
def get_environment_variables():
    return os.environ

# Set an environment variable
def set_environment_variable(key, value):
    os.environ[key] = value
    return True

# Remove an environment variable
def remove_environment_variable(key):
    try:
        del os.environ[key]
        return True
    except KeyError:
        print(f"Environment variable '{key}' does not exist.")
        return False
    

# Get the home directory of the current user
def get_home_directory():
    return os.path.expanduser('~')

# Get the temporary directory
def get_temp_directory():
    return os.path.join(get_home_directory(), 'tmp')

# Create a temporary file
def create_temp_file():
    import tempfile
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    return temp_file.name
