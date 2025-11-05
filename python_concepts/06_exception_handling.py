"""
Exception Handling in Python
============================
Try-except, custom exceptions, and error handling patterns
"""

# Basic exception handling
print("=== Basic Exception Handling ===")
def divide_numbers(a, b):
    """Safe division with exception handling"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Invalid input types!")
        return None

print(f"10 / 2 = {divide_numbers(10, 2)}")
print(f"10 / 0 = {divide_numbers(10, 0)}")
print(f"10 / 'a' = {divide_numbers(10, 'a')}")

# Multiple exception types
print("\n=== Multiple Exception Types ===")
def process_list(items, index):
    """Process list with multiple potential errors"""
    try:
        # Multiple operations that can fail
        value = items[index]
        result = 100 / value
        return f"Result: {result}"
    except IndexError:
        return "Error: Index out of range"
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid type for division"
    except Exception as e:
        return f"Unexpected error: {e}"

numbers = [1, 2, 0, 4, 5]
print(process_list(numbers, 1))  # Success
print(process_list(numbers, 10)) # IndexError
print(process_list(numbers, 2))  # ZeroDivisionError
print(process_list(['a', 'b'], 0))  # TypeError

# Try-except-else-finally
print("\n=== Try-Except-Else-Finally ===")
def read_file_safe(filename):
    """Demonstrate complete try-except structure"""
    file_handle = None
    try:
        print(f"Attempting to open {filename}")
        file_handle = open(filename, 'r')
        content = file_handle.read()
        print(f"File opened successfully")
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'")
        return None
    else:
        print("File read successfully (else block)")
    finally:
        print("Cleanup (finally block)")
        if file_handle and not file_handle.closed:
            file_handle.close()
            print("File closed")

# Test with non-existent file
content = read_file_safe("nonexistent.txt")

# Exception chaining
print("\n=== Exception Chaining ===")
def process_data(data):
    """Demonstrate exception chaining"""
    try:
        # First operation that might fail
        processed = [int(x) for x in data]
        return processed
    except ValueError as e:
        # Re-raise with additional context
        raise ValueError(f"Failed to process data: {data}") from e

def main_process():
    """Main function with chained exceptions"""
    try:
        invalid_data = ['1', '2', 'abc', '4']
        result = process_data(invalid_data)
        return result
    except ValueError as e:
        print(f"Main error: {e}")
        print(f"Original cause: {e.__cause__}")

main_process()

# Custom exceptions
print("\n=== Custom Exceptions ===")
class ValidationError(Exception):
    """Custom exception for validation errors"""
    
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

class AgeError(ValidationError):
    """Specific exception for age-related errors"""
    pass

class EmailError(ValidationError):
    """Specific exception for email-related errors"""
    pass

def validate_user(name, age, email):
    """Validate user data with custom exceptions"""
    if not name or len(name) < 2:
        raise ValidationError("Name must be at least 2 characters", "NAME_TOO_SHORT")
    
    if age < 0 or age > 150:
        raise AgeError(f"Invalid age: {age}. Must be between 0 and 150")
    
    if '@' not in email or '.' not in email:
        raise EmailError(f"Invalid email format: {email}")
    
    return {"name": name, "age": age, "email": email}

# Test custom exceptions
test_users = [
    ("John", 25, "john@email.com"),  # Valid
    ("", 25, "john@email.com"),      # Invalid name
    ("John", -5, "john@email.com"),  # Invalid age
    ("John", 25, "invalid-email")    # Invalid email
]

for name, age, email in test_users:
    try:
        user = validate_user(name, age, email)
        print(f"Valid user: {user}")
    except ValidationError as e:
        print(f"Validation error: {e}")
        if hasattr(e, 'error_code') and e.error_code:
            print(f"Error code: {e.error_code}")

# Context managers for exception safety
print("\n=== Context Managers ===")
class DatabaseConnection:
    """Mock database connection with context manager"""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False
    
    def __enter__(self):
        print(f"Opening connection to {self.db_name}")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing connection to {self.db_name}")
        self.connected = False
        if exc_type:
            print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
        return False  # Don't suppress exceptions
    
    def execute_query(self, query):
        if not self.connected:
            raise RuntimeError("Not connected to database")
        
        if "DROP" in query.upper():
            raise ValueError("DROP operations not allowed")
        
        return f"Executed: {query}"

# Using context manager
try:
    with DatabaseConnection("mydb") as db:
        result1 = db.execute_query("SELECT * FROM users")
        print(result1)
        
        # This will raise an exception
        result2 = db.execute_query("DROP TABLE users")
        print(result2)  # This won't be reached
        
except ValueError as e:
    print(f"Query error: {e}")

# Exception handling patterns
print("\n=== Exception Handling Patterns ===")

# 1. EAFP (Easier to Ask for Forgiveness than Permission)
def eafp_example(data, key):
    """EAFP pattern - try first, handle exceptions"""
    try:
        return data[key]
    except KeyError:
        return f"Key '{key}' not found"

# 2. LBYL (Look Before You Leap)
def lbyl_example(data, key):
    """LBYL pattern - check conditions first"""
    if key in data:
        return data[key]
    else:
        return f"Key '{key}' not found"

test_dict = {'a': 1, 'b': 2}
print(f"EAFP result: {eafp_example(test_dict, 'c')}")
print(f"LBYL result: {lbyl_example(test_dict, 'c')}")

# Exception logging
print("\n=== Exception Logging ===")
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, 
                   format='%(levelname)s - %(message)s')

def risky_operation(value):
    """Function that logs exceptions"""
    try:
        result = 10 / value
        logging.info(f"Operation successful: 10 / {value} = {result}")
        return result
    except ZeroDivisionError as e:
        logging.error(f"Division by zero error: {e}")
        raise
    except Exception as e:
        logging.exception(f"Unexpected error in risky_operation: {e}")
        raise

# Test logging
try:
    risky_operation(5)
    risky_operation(0)
except Exception:
    print("Caught and logged exception")

# Assertions
print("\n=== Assertions ===")
def calculate_average(numbers):
    """Calculate average with assertions for debugging"""
    assert len(numbers) > 0, "Cannot calculate average of empty list"
    assert all(isinstance(n, (int, float)) for n in numbers), "All items must be numbers"
    
    return sum(numbers) / len(numbers)

# Test assertions (only when __debug__ is True)
try:
    avg1 = calculate_average([1, 2, 3, 4, 5])
    print(f"Average: {avg1}")
    
    # This will raise AssertionError
    avg2 = calculate_average([])
except AssertionError as e:
    print(f"Assertion error: {e}")