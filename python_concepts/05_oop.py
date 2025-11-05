"""
Object-Oriented Programming in Python
====================================
Classes, Objects, Inheritance, and OOP Concepts
"""

# Basic class definition
print("=== Basic Class ===")
class Person:
    """A simple Person class"""
    
    # Class variable (shared by all instances)
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        """Constructor method"""
        self.name = name  # Instance variable
        self.age = age    # Instance variable
    
    def introduce(self):
        """Instance method"""
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    def have_birthday(self):
        """Method that modifies instance state"""
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age}"

# Creating objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.introduce())
print(person2.introduce())
print(f"Species: {Person.species}")
print(person1.have_birthday())

# Class methods and static methods
print("\n=== Class and Static Methods ===")
class MathUtils:
    """Utility class for mathematical operations"""
    
    pi = 3.14159
    
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def create_default(cls):
        """Class method - alternative constructor"""
        return cls("DefaultCalculator")
    
    @staticmethod
    def add(a, b):
        """Static method - doesn't need class or instance"""
        return a + b
    
    @staticmethod
    def circle_area(radius):
        """Calculate circle area"""
        return MathUtils.pi * radius ** 2

# Using class and static methods
calculator = MathUtils.create_default()
print(f"Calculator name: {calculator.name}")
print(f"Static add: {MathUtils.add(5, 3)}")
print(f"Circle area: {MathUtils.circle_area(5)}")

# Inheritance
print("\n=== Inheritance ===")
class Animal:
    """Base class"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return f"{self.name} makes a sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    """Derived class"""
    
    def __init__(self, name, breed):
        super().__init__(name, "Canis lupus")  # Call parent constructor
        self.breed = breed
    
    def make_sound(self):  # Override parent method
        return f"{self.name} barks: Woof!"
    
    def fetch(self):  # New method specific to Dog
        return f"{self.name} fetches the ball"

class Cat(Animal):
    """Another derived class"""
    
    def __init__(self, name, color):
        super().__init__(name, "Felis catus")
        self.color = color
    
    def make_sound(self):  # Override parent method
        return f"{self.name} meows: Meow!"
    
    def climb(self):  # New method specific to Cat
        return f"{self.name} climbs the tree"

# Using inheritance
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(dog.info())
print(dog.make_sound())
print(dog.fetch())

print(cat.info())
print(cat.make_sound())
print(cat.climb())

# Multiple inheritance
print("\n=== Multiple Inheritance ===")
class Flyable:
    """Mixin class for flying ability"""
    
    def fly(self):
        return f"{self.name} is flying"

class Swimmable:
    """Mixin class for swimming ability"""
    
    def swim(self):
        return f"{self.name} is swimming"

class Duck(Animal, Flyable, Swimmable):
    """Class with multiple inheritance"""
    
    def __init__(self, name):
        super().__init__(name, "Anas platyrhynchos")
    
    def make_sound(self):
        return f"{self.name} quacks: Quack!"

duck = Duck("Donald")
print(duck.info())
print(duck.make_sound())
print(duck.fly())
print(duck.swim())

# Property decorators
print("\n=== Properties ===")
class Circle:
    """Class demonstrating properties"""
    
    def __init__(self, radius):
        self._radius = radius  # Private attribute convention
    
    @property
    def radius(self):
        """Getter for radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Setter for radius with validation"""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self):
        """Calculated property"""
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self):
        """Another calculated property"""
        return 2 * 3.14159 * self._radius

circle = Circle(5)
print(f"Radius: {circle.radius}")
print(f"Area: {circle.area}")
print(f"Circumference: {circle.circumference}")

circle.radius = 10  # Using setter
print(f"New radius: {circle.radius}")
print(f"New area: {circle.area}")

# Special methods (magic methods)
print("\n=== Special Methods ===")
class Book:
    """Class demonstrating special methods"""
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """String representation for users"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """String representation for developers"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Length of the book"""
        return self.pages
    
    def __eq__(self, other):
        """Equality comparison"""
        if isinstance(other, Book):
            return (self.title == other.title and 
                   self.author == other.author)
        return False
    
    def __lt__(self, other):
        """Less than comparison (for sorting)"""
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented

book1 = Book("Python Programming", "John Doe", 300)
book2 = Book("Data Structures", "Jane Smith", 250)

print(f"Book 1: {book1}")  # Uses __str__
print(f"Book 1 repr: {repr(book1)}")  # Uses __repr__
print(f"Book 1 length: {len(book1)}")  # Uses __len__
print(f"Books equal: {book1 == book2}")  # Uses __eq__
print(f"Book1 < Book2: {book1 < book2}")  # Uses __lt__

# Abstract classes
print("\n=== Abstract Classes ===")
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class"""
    
    @abstractmethod
    def area(self):
        """Abstract method that must be implemented"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Another abstract method"""
        pass
    
    def description(self):
        """Concrete method in abstract class"""
        return f"This is a {self.__class__.__name__}"

class Rectangle(Shape):
    """Concrete implementation of Shape"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 3)
print(f"Rectangle description: {rectangle.description()}")
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")

# Class composition
print("\n=== Composition ===")
class Engine:
    """Component class"""
    
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine with {self.horsepower} HP started"

class Car:
    """Class using composition"""
    
    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)  # Composition
    
    def start_car(self):
        return f"{self.make} {self.model}: {self.engine.start()}"

car = Car("Toyota", "Camry", 200)
print(car.start_car())