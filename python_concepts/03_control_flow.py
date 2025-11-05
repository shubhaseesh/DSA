"""
Python Control Flow Examples
===========================
If-else, Loops, and Control Statements
"""

# If-else statements
print("=== If-Else Statements ===")
age = 18
score = 85

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Multiple conditions
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Score: {score}, Grade: {grade}")

# Ternary operator
status = "Pass" if score >= 60 else "Fail"
print(f"Status: {status}")

# For loops
print("\n=== For Loops ===")
fruits = ['apple', 'banana', 'orange']

# Basic for loop
print("Fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# Loop with index
print("Fruits with index:")
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

# Range function
print("Numbers 1 to 5:")
for i in range(1, 6):
    print(f"  {i}")

# Step in range
print("Even numbers 0 to 10:")
for i in range(0, 11, 2):
    print(f"  {i}")

# Loop through dictionary
student = {'name': 'John', 'age': 20, 'grade': 'A'}
print("Student details:")
for key, value in student.items():
    print(f"  {key}: {value}")

# While loops
print("\n=== While Loops ===")
count = 1
print("Counting to 5:")
while count <= 5:
    print(f"  Count: {count}")
    count += 1

# While with condition
number = 1
print("Powers of 2 less than 100:")
while number < 100:
    print(f"  {number}")
    number *= 2

# Break and Continue
print("\n=== Break and Continue ===")
print("Numbers 1 to 10, skip 5, stop at 8:")
for i in range(1, 11):
    if i == 5:
        continue  # Skip 5
    if i == 8:
        break     # Stop at 8
    print(f"  {i}")

# Nested loops
print("\n=== Nested Loops ===")
print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()  # New line after each row

# Loop with else
print("\n=== Loop with Else ===")
numbers = [2, 4, 6, 8, 10]
for num in numbers:
    if num % 2 != 0:
        print(f"Found odd number: {num}")
        break
else:
    print("All numbers are even")

# List comprehension with conditions
print("\n=== List Comprehension with Conditions ===")
numbers = range(1, 11)
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Match-case (Python 3.10+)
print("\n=== Match-Case (Python 3.10+) ===")
def describe_animal(animal):
    match animal:
        case "dog":
            return "Loyal companion"
        case "cat":
            return "Independent hunter"
        case "bird":
            return "Flying friend"
        case _:  # Default case
            return "Unknown animal"

animals = ["dog", "cat", "fish"]
for animal in animals:
    description = describe_animal(animal)
    print(f"{animal}: {description}")