"""
Python Data Structures Examples
==============================
Lists, Tuples, Sets, and Dictionaries
"""

# Lists
print("=== Lists ===")
fruits = ['apple', 'banana', 'orange']
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'hello', 3.14, True]

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")

# List operations
fruits.append('grape')
print(f"After append: {fruits}")
fruits.insert(1, 'mango')
print(f"After insert: {fruits}")
fruits.remove('banana')
print(f"After remove: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Slicing [1:3]: {fruits[1:3]}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"Squares: {squares}")
print(f"Even numbers: {even_numbers}")

# Tuples
print("\n=== Tuples ===")
coordinates = (10, 20)
person = ('John', 25, 'Engineer')
single_tuple = (42,)  # Note the comma

print(f"Coordinates: {coordinates}")
print(f"Person: {person}")
print(f"Single tuple: {single_tuple}")

# Tuple unpacking
x, y = coordinates
name, age, job = person
print(f"Unpacked coordinates: x={x}, y={y}")
print(f"Unpacked person: {name}, {age}, {job}")

# Sets
print("\n=== Sets ===")
unique_numbers = {1, 2, 3, 4, 5}
fruits_set = {'apple', 'banana', 'orange', 'apple'}  # Duplicates removed

print(f"Unique numbers: {unique_numbers}")
print(f"Fruits set: {fruits_set}")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")

# Dictionaries
print("\n=== Dictionaries ===")
student = {
    'name': 'Alice',
    'age': 20,
    'grades': [85, 90, 78],
    'is_enrolled': True
}

print(f"Student: {student}")
print(f"Name: {student['name']}")
print(f"Age: {student.get('age')}")

# Dictionary operations
student['email'] = 'alice@example.com'
student['age'] = 21
print(f"Updated student: {student}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dictionary: {squares_dict}")

# Nested structures
school = {
    'students': [
        {'name': 'Alice', 'grade': 'A'},
        {'name': 'Bob', 'grade': 'B'}
    ],
    'teachers': ['Mr. Smith', 'Ms. Johnson']
}
print(f"School: {school}")
print(f"First student: {school['students'][0]['name']}")