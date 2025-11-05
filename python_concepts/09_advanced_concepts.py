"""
Advanced Python Concepts
=======================
Decorators, generators, context managers, and more
"""

# Decorators
print("=== Decorators ===")

# Simple decorator
def my_decorator(func):
    """Simple decorator that adds behavior before and after function call"""
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Function with decorator"""
    print(f"Hello, {name}!")
    return f"Greeted {name}"

result = greet("Alice")
print(f"Result: {result}")

# Decorator with parameters
def repeat(times):
    """Decorator that repeats function execution"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                print(f"Execution #{i+1}")
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    """Function that will be repeated"""
    print("Hello!")
    return "Done"

results = say_hello()
print(f"Results: {results}")

# Class-based decorator
print("\n=== Class-based Decorators ===")
class CountCalls:
    """Decorator class that counts function calls"""
    
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} called {self.count} time(s)")
        return self.func(*args, **kwargs)

@CountCalls
def add_numbers(a, b):
    """Function with call counter"""
    return a + b

print(f"5 + 3 = {add_numbers(5, 3)}")
print(f"10 + 7 = {add_numbers(10, 7)}")
print(f"2 + 8 = {add_numbers(2, 8)}")

# Property decorator
print("\n=== Property Decorators ===")
class Temperature:
    """Class demonstrating property decorators"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature using Fahrenheit"""
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """Get temperature in Kelvin"""
        return self._celsius + 273.15

temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F = {temp.kelvin}K")

temp.fahrenheit = 86
print(f"After setting to 86°F: {temp.celsius}°C = {temp.fahrenheit}°F = {temp.kelvin}K")

# Generators
print("\n=== Generators ===")

# Simple generator
def count_up_to(max_count):
    """Generator that counts up to max_count"""
    count = 1
    while count <= max_count:
        yield count
        count += 1

print("Counting up to 5:")
for num in count_up_to(5):
    print(f"  {num}")

# Generator with send()
def accumulator():
    """Generator that accumulates values"""
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

acc = accumulator()
next(acc)  # Initialize generator
print(f"Accumulator initialized: {acc.send(10)}")
print(f"Added 5: {acc.send(5)}")
print(f"Added 20: {acc.send(20)}")

# Generator expression
squares_gen = (x**2 for x in range(1, 6))
print(f"Generator expression - squares: {list(squares_gen)}")

# Fibonacci generator
def fibonacci_generator():
    """Generate Fibonacci sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("First 10 Fibonacci numbers:")
fib_gen = fibonacci_generator()
for i in range(10):
    print(f"  F({i}) = {next(fib_gen)}")

# Context Managers
print("\n=== Context Managers ===")

# Function-based context manager
from contextlib import contextmanager

@contextmanager
def timer():
    """Context manager to time code execution"""
    import time
    start = time.time()
    print("Timer started")
    try:
        yield start
    finally:
        end = time.time()
        print(f"Timer ended. Elapsed time: {end - start:.4f} seconds")

with timer() as start_time:
    # Simulate some work
    import time
    time.sleep(0.1)
    print(f"Doing work... (started at {start_time})")

# Class-based context manager
class DatabaseConnection:
    """Mock database connection context manager"""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False
    
    def __enter__(self):
        print(f"Connecting to database: {self.db_name}")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Disconnecting from database: {self.db_name}")
        self.connected = False
        if exc_type:
            print(f"Exception occurred: {exc_type.__name__}")
        return False  # Don't suppress exceptions
    
    def query(self, sql):
        """Execute a query"""
        if not self.connected:
            raise RuntimeError("Not connected to database")
        return f"Result for: {sql}"

with DatabaseConnection("mydb") as db:
    result = db.query("SELECT * FROM users")
    print(f"Query result: {result}")

# Iterators
print("\n=== Iterators ===")

class NumberRange:
    """Custom iterator class"""
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        self.start += 1
        return self.start - 1

print("Custom iterator (0 to 5):")
for num in NumberRange(0, 5):
    print(f"  {num}")

# Metaclasses (advanced)
print("\n=== Metaclasses ===")

class SingletonMeta(type):
    """Metaclass that creates singleton instances"""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseManager(metaclass=SingletonMeta):
    """Singleton class using metaclass"""
    
    def __init__(self):
        self.connection = "Connected to database"
    
    def get_connection(self):
        return self.connection

# Test singleton
db1 = DatabaseManager()
db2 = DatabaseManager()
print(f"Same instance? {db1 is db2}")
print(f"Connection: {db1.get_connection()}")

# Descriptors
print("\n=== Descriptors ===")

class ValidatedAttribute:
    """Descriptor for validated attributes"""
    
    def __init__(self, name, validator=None):
        self.name = name
        self.validator = validator
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        if self.validator and not self.validator(value):
            raise ValueError(f"Invalid value for {self.name}: {value}")
        obj.__dict__[self.name] = value
    
    def __delete__(self, obj):
        del obj.__dict__[self.name]

class Person:
    """Class using descriptors"""
    
    name = ValidatedAttribute('name', lambda x: isinstance(x, str) and len(x) > 0)
    age = ValidatedAttribute('age', lambda x: isinstance(x, int) and 0 <= x <= 150)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(f"Person: {person.name}, age {person.age}")

try:
    person.age = -5  # This will raise ValueError
except ValueError as e:
    print(f"Validation error: {e}")

# Closures
print("\n=== Closures ===")

def create_multiplier(factor):
    """Create a multiplier function with closure"""
    def multiplier(x):
        return x * factor
    return multiplier

multiply_by_3 = create_multiplier(3)
multiply_by_10 = create_multiplier(10)

print(f"3 * 7 = {multiply_by_3(7)}")
print(f"10 * 4 = {multiply_by_10(4)}")

# Function with memory using closure
def create_counter(initial=0):
    """Create a counter function with memory"""
    count = initial
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    def reset():
        nonlocal count
        count = initial
    
    counter.reset = reset
    return counter

counter1 = create_counter(10)
counter2 = create_counter(100)

print(f"Counter1: {counter1()}")  # 11
print(f"Counter1: {counter1()}")  # 12
print(f"Counter2: {counter2()}")  # 101
counter1.reset()
print(f"Counter1 after reset: {counter1()}")  # 11

# Function annotations and type hints
print("\n=== Type Hints and Annotations ===")

from typing import List, Dict, Optional, Union, Callable

def process_data(
    numbers: List[int], 
    multiplier: float = 1.0,
    formatter: Optional[Callable[[float], str]] = None
) -> Dict[str, Union[int, float, List[float]]]:
    """
    Process a list of numbers with type hints
    
    Args:
        numbers: List of integers to process
        multiplier: Factor to multiply each number
        formatter: Optional function to format results
    
    Returns:
        Dictionary with processed data
    """
    processed = [num * multiplier for num in numbers]
    
    result = {
        'original_count': len(numbers),
        'sum': sum(processed),
        'average': sum(processed) / len(processed) if processed else 0,
        'processed_values': processed
    }
    
    if formatter:
        result['formatted'] = [formatter(val) for val in processed]
    
    return result

# Test type-hinted function
numbers = [1, 2, 3, 4, 5]
result = process_data(numbers, 2.5, lambda x: f"{x:.1f}")
print(f"Processed data: {result}")

# Async/await preview (basic example)
print("\n=== Async Programming Concepts ===")

import asyncio

async def async_task(name: str, delay: float) -> str:
    """Asynchronous task simulation"""
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} completed after {delay} seconds")
    return f"Result from {name}"

async def run_async_demo():
    """Run multiple async tasks"""
    # Run tasks concurrently
    tasks = [
        async_task("Task1", 0.1),
        async_task("Task2", 0.2),
        async_task("Task3", 0.15)
    ]
    
    results = await asyncio.gather(*tasks)
    return results

# Note: This would normally be run with asyncio.run() in a script
print("Async demo (conceptual - would run concurrently in practice)")

print("\nAdvanced Python concepts demonstration complete!")