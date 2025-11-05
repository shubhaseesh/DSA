"""
File I/O and Working with Files in Python
=========================================
Reading, writing, and manipulating files
"""

import os
import json
import csv
from pathlib import Path

# Basic file operations
print("=== Basic File Operations ===")

# Writing to a file
def create_sample_file():
    """Create a sample text file"""
    content = """This is line 1
This is line 2
This is line 3
Numbers: 1, 2, 3, 4, 5
End of file"""
    
    with open('sample.txt', 'w') as file:
        file.write(content)
    print("Created sample.txt")

create_sample_file()

# Reading entire file
def read_entire_file(filename):
    """Read and display entire file content"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")
    except FileNotFoundError:
        print(f"File {filename} not found")

read_entire_file('sample.txt')

# Reading file line by line
print("\n=== Reading Line by Line ===")
def read_lines(filename):
    """Read file line by line"""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, 1):
                print(f"Line {i}: {line.strip()}")
    except FileNotFoundError:
        print(f"File {filename} not found")

read_lines('sample.txt')

# Different file modes
print("\n=== File Modes ===")
def demonstrate_file_modes():
    """Demonstrate different file opening modes"""
    
    # Append mode
    with open('sample.txt', 'a') as file:
        file.write('\nAppended line')
    print("Appended to file")
    
    # Read and write mode
    with open('sample.txt', 'r+') as file:
        content = file.read()
        file.seek(0)  # Go back to beginning
        file.write("MODIFIED: " + content)
    print("Modified file using r+ mode")

demonstrate_file_modes()

# Working with binary files
print("\n=== Binary Files ===")
def work_with_binary():
    """Demonstrate binary file operations"""
    
    # Write binary data
    data = b"This is binary data\x00\x01\x02\x03"
    with open('binary_file.bin', 'wb') as file:
        file.write(data)
    print("Created binary file")
    
    # Read binary data
    with open('binary_file.bin', 'rb') as file:
        binary_content = file.read()
        print(f"Binary content: {binary_content}")
        print(f"As text: {binary_content.decode('utf-8', errors='ignore')}")

work_with_binary()

# File position and seeking
print("\n=== File Position and Seeking ===")
def demonstrate_seeking():
    """Demonstrate file position manipulation"""
    
    with open('sample.txt', 'r') as file:
        print(f"Initial position: {file.tell()}")
        
        # Read first 10 characters
        chunk = file.read(10)
        print(f"Read: '{chunk}'")
        print(f"Position after read: {file.tell()}")
        
        # Seek to position 20
        file.seek(20)
        print(f"Position after seek(20): {file.tell()}")
        
        # Read next 10 characters
        chunk = file.read(10)
        print(f"Read from position 20: '{chunk}'")
        
        # Seek from end
        file.seek(-10, 2)  # 10 characters from end
        print(f"Position 10 from end: {file.tell()}")
        chunk = file.read()
        print(f"Read from near end: '{chunk}'")

demonstrate_seeking()

# Working with CSV files
print("\n=== CSV Files ===")
def work_with_csv():
    """Demonstrate CSV file operations"""
    
    # Create CSV data
    students = [
        ['Name', 'Age', 'Grade', 'Subject'],
        ['Alice', 20, 'A', 'Math'],
        ['Bob', 21, 'B', 'Physics'],
        ['Charlie', 19, 'A', 'Chemistry'],
        ['Diana', 22, 'B+', 'Biology']
    ]
    
    # Write CSV file
    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)
    print("Created students.csv")
    
    # Read CSV file
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        print("CSV content:")
        for row_num, row in enumerate(reader):
            print(f"  Row {row_num}: {row}")
    
    # Read CSV as dictionary
    with open('students.csv', 'r') as file:
        dict_reader = csv.DictReader(file)
        print("CSV as dictionaries:")
        for row in dict_reader:
            print(f"  {row}")

work_with_csv()

# Working with JSON files
print("\n=== JSON Files ===")
def work_with_json():
    """Demonstrate JSON file operations"""
    
    # Create sample data
    data = {
        "students": [
            {"name": "Alice", "age": 20, "grades": [85, 90, 88]},
            {"name": "Bob", "age": 21, "grades": [78, 82, 80]},
            {"name": "Charlie", "age": 19, "grades": [92, 95, 89]}
        ],
        "course": "Python Programming",
        "semester": "Fall 2024"
    }
    
    # Write JSON file
    with open('course_data.json', 'w') as file:
        json.dump(data, file, indent=2)
    print("Created course_data.json")
    
    # Read JSON file
    with open('course_data.json', 'r') as file:
        loaded_data = json.load(file)
        print("Loaded JSON data:")
        print(f"  Course: {loaded_data['course']}")
        print(f"  Semester: {loaded_data['semester']}")
        print("  Students:")
        for student in loaded_data['students']:
            avg_grade = sum(student['grades']) / len(student['grades'])
            print(f"    {student['name']} (Age {student['age']}): Avg = {avg_grade:.1f}")

work_with_json()

# File and directory operations
print("\n=== File and Directory Operations ===")
def file_directory_ops():
    """Demonstrate file and directory operations"""
    
    # Create directory
    os.makedirs('test_directory', exist_ok=True)
    print("Created directory: test_directory")
    
    # List directory contents
    current_files = os.listdir('.')
    print(f"Current directory files: {current_files[:5]}...")  # Show first 5
    
    # Check if file exists
    files_to_check = ['sample.txt', 'nonexistent.txt']
    for filename in files_to_check:
        exists = os.path.exists(filename)
        print(f"File '{filename}' exists: {exists}")
    
    # Get file information
    if os.path.exists('sample.txt'):
        stat_info = os.stat('sample.txt')
        print(f"Sample.txt size: {stat_info.st_size} bytes")
        print(f"Last modified: {stat_info.st_mtime}")
    
    # Copy file content manually
    if os.path.exists('sample.txt'):
        with open('sample.txt', 'r') as source:
            with open('test_directory/copy_of_sample.txt', 'w') as dest:
                dest.write(source.read())
        print("Copied sample.txt to test_directory/")

file_directory_ops()

# Using pathlib (modern approach)
print("\n=== Using Pathlib ===")
def use_pathlib():
    """Demonstrate pathlib usage"""
    
    # Create Path objects
    current_dir = Path('.')
    sample_file = Path('sample.txt')
    
    print(f"Current directory: {current_dir.absolute()}")
    print(f"Sample file exists: {sample_file.exists()}")
    print(f"Sample file size: {sample_file.stat().st_size if sample_file.exists() else 'N/A'}")
    
    # Work with path components
    full_path = current_dir / 'test_directory' / 'new_file.txt'
    print(f"Constructed path: {full_path}")
    print(f"Parent directory: {full_path.parent}")
    print(f"Filename: {full_path.name}")
    print(f"File extension: {full_path.suffix}")
    
    # Create file using pathlib
    full_path.parent.mkdir(exist_ok=True)
    full_path.write_text("Created using pathlib")
    print(f"Created file: {full_path}")
    
    # Read using pathlib
    content = full_path.read_text()
    print(f"File content: {content}")
    
    # List files with pattern
    txt_files = list(current_dir.glob('*.txt'))
    print(f"Text files in current directory: {[f.name for f in txt_files]}")

use_pathlib()

# Error handling with files
print("\n=== File Error Handling ===")
def safe_file_operations():
    """Demonstrate safe file operations with error handling"""
    
    def safe_read_file(filename):
        """Safely read a file with proper error handling"""
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return f"Error: File '{filename}' not found"
        except PermissionError:
            return f"Error: Permission denied for '{filename}'"
        except UnicodeDecodeError:
            return f"Error: Cannot decode '{filename}' as text"
        except Exception as e:
            return f"Unexpected error reading '{filename}': {e}"
    
    # Test with various files
    test_files = ['sample.txt', 'nonexistent.txt', 'binary_file.bin']
    
    for filename in test_files:
        result = safe_read_file(filename)
        print(f"Reading {filename}: {result[:50]}{'...' if len(str(result)) > 50 else ''}")

safe_file_operations()

# Context manager for file operations
print("\n=== Custom File Context Manager ===")
class FileManager:
    """Custom context manager for file operations"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening file: {self.filename}")
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except Exception as e:
            print(f"Error opening file: {e}")
            raise
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            print(f"Closing file: {self.filename}")
            self.file.close()
        
        if exc_type:
            print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
        
        return False  # Don't suppress exceptions

# Use custom context manager
try:
    with FileManager('sample.txt', 'r') as f:
        content = f.read(50)  # Read first 50 characters
        print(f"Content preview: {content}")
except Exception as e:
    print(f"Error using FileManager: {e}")

# Cleanup
print("\n=== Cleanup ===")
def cleanup_files():
    """Clean up created files"""
    files_to_remove = ['sample.txt', 'binary_file.bin', 'students.csv', 'course_data.json']
    
    for filename in files_to_remove:
        try:
            if os.path.exists(filename):
                os.remove(filename)
                print(f"Removed {filename}")
        except Exception as e:
            print(f"Error removing {filename}: {e}")
    
    # Remove directory and its contents
    try:
        import shutil
        if os.path.exists('test_directory'):
            shutil.rmtree('test_directory')
            print("Removed test_directory")
    except Exception as e:
        print(f"Error removing directory: {e}")

cleanup_files()
print("File operations demonstration complete!")