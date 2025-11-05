"""
Python Functions Examples
========================
Function definitions, arguments, and advanced concepts
"""

# Basic function
print("=== Basic Functions ===")
def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

print(greet("Alice"))

# Function with multiple parameters
def add_numbers(a, b):
    """Add two numbers"""
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Function with default parameters
print("\n=== Default Parameters ===")
def greet_with_title(name, title="Mr."):
    """Greet with optional title"""
    return f"Hello, {title} {name}!"

print(greet_with_title("Smith"))
print(greet_with_title("Johnson", "Dr."))

# Function with variable arguments (*args)
print("\n=== Variable Arguments (*args) ===")
def sum_all(*numbers):
    """Sum all provided numbers"""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1,2,3: {sum_all(1, 2, 3)}")
print(f"Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")

# Function with keyword arguments (**kwargs)
print("\n=== Keyword Arguments (**kwargs) ===")
def print_info(**info):
    """Print all provided information"""
    for key, value in info.items():
        print(f"  {key}: {value}")

print("Student information:")
print_info(name="Alice", age=20, grade="A", city="New York")

# Function with both *args and **kwargs
print("\n=== Mixed Arguments ===")
def flexible_function(required, *args, **kwargs):
    """Function with all types of arguments"""
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

flexible_function("must_have", 1, 2, 3, name="Bob", age=25)

# Lambda functions
print("\n=== Lambda Functions ===")
square = lambda x: x ** 2
add = lambda x, y: x + y

print(f"Square of 5: {square(5)}")
print(f"Add 3 and 7: {add(3, 7)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Original: {numbers}")
print(f"Squared: {squared}")
print(f"Even: {even_numbers}")

# Higher-order functions
print("\n=== Higher-Order Functions ===")
def apply_operation(numbers, operation):
    """Apply operation to all numbers"""
    return [operation(num) for num in numbers]

def double(x):
    return x * 2

def cube(x):
    return x ** 3

numbers = [1, 2, 3, 4]
doubled = apply_operation(numbers, double)
cubed = apply_operation(numbers, cube)

print(f"Original: {numbers}")
print(f"Doubled: {doubled}")
print(f"Cubed: {cubed}")

# Decorators
print("\n=== Decorators ===")
def timing_decorator(func):
    """Decorator to time function execution"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    """A function that takes some time"""
    import time
    time.sleep(0.1)
    return "Done!"

result = slow_function()
print(f"Result: {result}")

# Recursive functions
print("\n=== Recursive Functions ===")
def factorial(n):
    """Calculate factorial recursively"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Factorial of 5: {factorial(5)}")
print(f"Fibonacci sequence (first 10):")
for i in range(10):
    print(f"  F({i}) = {fibonacci(i)}")

# Generators
print("\n=== Generators ===")
def number_generator(max_num):
    """Generate numbers up to max_num"""
    num = 0
    while num < max_num:
        yield num
        num += 1

print("Generated numbers:")
for num in number_generator(5):
    print(f"  {num}")

# Generator expression
squares_gen = (x**2 for x in range(5))
print(f"Generated squares: {list(squares_gen)}")

# Function annotations (type hints)
print("\n=== Type Hints ===")
def calculate_area(length: float, width: float) -> float:
    """Calculate rectangle area with type hints"""
    return length * width

area = calculate_area(5.0, 3.0)
print(f"Area: {area}")

# Docstrings and help
print("\n=== Function Documentation ===")
def complex_function(param1: int, param2: str = "default") -> dict:
    """
    A complex function demonstrating documentation.
    
    Args:
        param1 (int): The first parameter
        param2 (str): The second parameter with default value
        
    Returns:
        dict: A dictionary containing the parameters
        
    Examples:
        >>> complex_function(42, "hello")
        {'param1': 42, 'param2': 'hello'}
    """
    return {'param1': param1, 'param2': param2}

result = complex_function(42, "hello")
print(f"Function result: {result}")
print(f"Function help: {complex_function.__doc__}")