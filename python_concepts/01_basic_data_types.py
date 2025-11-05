"""
Python Basic Data Types Examples
===============================
"""

# Numbers
print("=== Numbers ===")
integer_num = 42
float_num = 3.14159
complex_num = 3 + 4j

print(f"Integer: {integer_num} (type: {type(integer_num)})")
print(f"Float: {float_num} (type: {type(float_num)})")
print(f"Complex: {complex_num} (type: {type(complex_num)})")

# Strings
print("\n=== Strings ===")
single_quote = 'Hello'
double_quote = "World"
multiline = """This is a
multiline string"""
f_string = f"Combined: {single_quote} {double_quote}"

print(f"Single quote: {single_quote}")
print(f"Double quote: {double_quote}")
print(f"F-string: {f_string}")
print(f"Multiline: {repr(multiline)}")

# String methods
text = "Python Programming"
print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Split: {text.split()}")
print(f"Replace: {text.replace('Python', 'Java')}")
print(f"Length: {len(text)}")

# Booleans
print("\n=== Booleans ===")
is_true = True
is_false = False
print(f"True: {is_true}")
print(f"False: {is_false}")
print(f"Boolean from number: {bool(1)} and {bool(0)}")
print(f"Boolean from string: {bool('hello')} and {bool('')}")

# None type
print("\n=== None Type ===")
nothing = None
print(f"None value: {nothing} (type: {type(nothing)})")