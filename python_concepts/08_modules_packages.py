"""
Python Modules and Packages
===========================
Creating, importing, and organizing code
"""

# Standard library imports
import math
import random
import datetime
from collections import defaultdict, Counter
from itertools import combinations, permutations

print("=== Standard Library Modules ===")

# Math module
print(f"Math constants:")
print(f"  π = {math.pi}")
print(f"  e = {math.e}")
print(f"  √16 = {math.sqrt(16)}")
print(f"  sin(π/2) = {math.sin(math.pi/2)}")
print(f"  log(100, 10) = {math.log(100, 10)}")

# Random module
print(f"\nRandom operations:")
print(f"  Random float [0,1): {random.random()}")
print(f"  Random int [1,10]: {random.randint(1, 10)}")
print(f"  Random choice: {random.choice(['apple', 'banana', 'orange'])}")
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"  Shuffled list: {numbers}")

# Datetime module
print(f"\nDate and time:")
now = datetime.datetime.now()
print(f"  Current time: {now}")
print(f"  Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"  Date only: {now.date()}")
print(f"  Time only: {now.time()}")

# Collections module
print(f"\nCollections:")
# defaultdict
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
dd['vegetables'].append('carrot')
print(f"  defaultdict: {dict(dd)}")

# Counter
text = "hello world"
counter = Counter(text)
print(f"  Character count: {counter}")
print(f"  Most common: {counter.most_common(3)}")

# Itertools module
print(f"\nItertools:")
items = ['A', 'B', 'C']
print(f"  Combinations of 2: {list(combinations(items, 2))}")
print(f"  Permutations of 2: {list(permutations(items, 2))}")

# Creating a simple module
print("\n=== Creating Custom Modules ===")

# Create a math utilities module
math_utils_code = '''
"""
Math Utilities Module
====================
Custom mathematical functions
"""

def factorial(n):
    """Calculate factorial of n"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Generate fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(n):
    """Find prime factors of a number"""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

# Module-level variable
PI = 3.14159265359

# Module-level function that runs on import
def _initialize():
    """Private function (convention with underscore)"""
    print("Math utils module initialized")

if __name__ == "__main__":
    # This code runs only when module is executed directly
    print("Testing math_utils module:")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Fibonacci(10): {fibonacci(10)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Prime factors of 60: {prime_factors(60)}")
'''

# Write the module to a file
with open('math_utils.py', 'w') as f:
    f.write(math_utils_code)

print("Created math_utils.py module")

# Import and use the custom module
import math_utils

print(f"Using custom module:")
print(f"  Factorial of 6: {math_utils.factorial(6)}")
print(f"  Fibonacci(8): {math_utils.fibonacci(8)}")
print(f"  Is 23 prime? {math_utils.is_prime(23)}")
print(f"  PI constant: {math_utils.PI}")

# Different import styles
print("\n=== Different Import Styles ===")

# Import specific functions
from math_utils import fibonacci, is_prime
print(f"Direct function call - Fibonacci(5): {fibonacci(5)}")
print(f"Direct function call - Is 11 prime? {is_prime(11)}")

# Import with alias
import math_utils as mu
print(f"With alias - Prime factors of 30: {mu.prime_factors(30)}")

# Import all (not recommended for production code)
# from math_utils import *  # Commented out to avoid namespace pollution

# Create a package structure
print("\n=== Creating Packages ===")

import os

# Create package directory
os.makedirs('mypackage', exist_ok=True)

# Create __init__.py
init_code = '''
"""
My Custom Package
================
A sample package demonstrating Python package structure
"""

# Package-level imports
from .calculator import Calculator
from .string_utils import StringProcessor
from . import data_structures

# Package metadata
__version__ = "1.0.0"
__author__ = "Your Name"

# Package-level variables
PACKAGE_NAME = "mypackage"

def get_info():
    """Get package information"""
    return {
        "name": PACKAGE_NAME,
        "version": __version__,
        "author": __author__
    }
'''

with open('mypackage/__init__.py', 'w') as f:
    f.write(init_code)

# Create calculator module
calculator_code = '''
"""
Calculator Module
================
Basic calculator operations
"""

class Calculator:
    """A simple calculator class"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Add two numbers"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract two numbers"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        """Get calculation history"""
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()

# Module-level convenience functions
def quick_add(a, b):
    """Quick addition without history"""
    return a + b

def quick_multiply(a, b):
    """Quick multiplication without history"""
    return a * b
'''

with open('mypackage/calculator.py', 'w') as f:
    f.write(calculator_code)

# Create string utilities module
string_utils_code = '''
"""
String Utilities Module
======================
String processing utilities
"""

class StringProcessor:
    """String processing utilities"""
    
    @staticmethod
    def reverse_string(text):
        """Reverse a string"""
        return text[::-1]
    
    @staticmethod
    def count_words(text):
        """Count words in text"""
        return len(text.split())
    
    @staticmethod
    def capitalize_words(text):
        """Capitalize each word"""
        return ' '.join(word.capitalize() for word in text.split())
    
    @staticmethod
    def remove_duplicates(text):
        """Remove duplicate characters while preserving order"""
        seen = set()
        result = []
        for char in text:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)
    
    @classmethod
    def analyze_text(cls, text):
        """Comprehensive text analysis"""
        return {
            'length': len(text),
            'word_count': cls.count_words(text),
            'unique_chars': len(set(text)),
            'uppercase_count': sum(1 for c in text if c.isupper()),
            'lowercase_count': sum(1 for c in text if c.islower()),
            'digit_count': sum(1 for c in text if c.isdigit())
        }

# Module-level utility functions
def clean_text(text):
    """Clean and normalize text"""
    import re
    # Remove extra whitespace and special characters
    cleaned = re.sub(r'\\s+', ' ', text.strip())
    return cleaned

def text_to_morse(text):
    """Convert text to Morse code (simplified)"""
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': '/'
    }
    return ' '.join(morse_dict.get(char.upper(), '?') for char in text)
'''

with open('mypackage/string_utils.py', 'w') as f:
    f.write(string_utils_code)

# Create data structures module
data_structures_code = '''
"""
Data Structures Module
=====================
Custom data structures
"""

class Stack:
    """Simple stack implementation"""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Get stack size"""
        return len(self.items)

class Queue:
    """Simple queue implementation"""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to rear of queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return front item"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    def front(self):
        """Return front item without removing"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Get queue size"""
        return len(self.items)
'''

with open('mypackage/data_structures.py', 'w') as f:
    f.write(data_structures_code)

print("Created package 'mypackage' with modules")

# Import and use the package
print("\n=== Using Custom Package ===")
import mypackage

# Use package info
info = mypackage.get_info()
print(f"Package info: {info}")

# Use calculator
calc = mypackage.Calculator()
print(f"Calculator: 10 + 5 = {calc.add(10, 5)}")
print(f"Calculator: 20 * 3 = {calc.multiply(20, 3)}")
print(f"History: {calc.get_history()}")

# Use string processor
processor = mypackage.StringProcessor()
text = "Hello World Python"
print(f"Original text: {text}")
print(f"Reversed: {processor.reverse_string(text)}")
print(f"Analysis: {processor.analyze_text(text)}")

# Use data structures
from mypackage.data_structures import Stack, Queue

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"Stack size: {stack.size()}")
print(f"Stack top: {stack.peek()}")
print(f"Popped: {stack.pop()}")

# Module search path
print("\n=== Module Search Path ===")
import sys
print("Python module search path:")
for i, path in enumerate(sys.path[:5]):  # Show first 5 paths
    print(f"  {i+1}. {path}")
print("  ... (more paths)")

# Module attributes
print("\n=== Module Attributes ===")
print(f"Math module file: {math.__file__}")
print(f"Math module name: {math.__name__}")
print(f"Available in math: {[attr for attr in dir(math) if not attr.startswith('_')][:10]}...")

# Conditional imports
print("\n=== Conditional Imports ===")
def safe_import_demo():
    """Demonstrate safe importing"""
    try:
        import numpy as np
        print("NumPy is available")
        return True
    except ImportError:
        print("NumPy not available, using alternatives")
        return False

    try:
        import requests
        print("Requests library is available")
    except ImportError:
        print("Requests not available, using urllib instead")

safe_import_demo()

# Cleanup
print("\n=== Cleanup ===")
import shutil

try:
    if os.path.exists('math_utils.py'):
        os.remove('math_utils.py')
        print("Removed math_utils.py")
    
    if os.path.exists('mypackage'):
        shutil.rmtree('mypackage')
        print("Removed mypackage directory")
except Exception as e:
    print(f"Cleanup error: {e}")

print("Modules and packages demonstration complete!")