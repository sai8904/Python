#!/usr/bin/env python3
"""
Python Practice - Core Concepts with Examples
Author: [Your Name]
"""

# ============================================
# 1. VARIABLES & DATA TYPES
# ============================================

def basic_concepts():
    print("=" * 50)
    print("1. CORE PYTHON BASICS")
    print("=" * 50)
    
    # Variables
    name = "John"
    age = 25
    salary = 50000.50
    is_active = True
    
    print(f"Name: {name}, Age: {age}, Salary: {salary}, Active: {is_active}")
    
    # Type casting
    num_str = "123"
    num_int = int(num_str)
    num_float = float(num_int)
    print(f"Casting: '{num_str}' -> {num_int} -> {num_float}")
    
    # Type checking
    print(f"Type of age: {type(age)}")
    print(f"Type of salary: {type(salary)}")

# ============================================
# 2. DATA STRUCTURES
# ============================================

def data_structures():
    print("\n" + "=" * 50)
    print("2. DATA STRUCTURES")
    print("=" * 50)
    
    # Lists - Ordered, mutable
    fruits = ["apple", "banana", "orange"]
    fruits.append("grape")
    fruits.remove("banana")
    print(f"List: {fruits}")
    print(f"First item: {fruits[0]}")
    print(f"Slicing: {fruits[1:3]}")
    
    # List comprehension
    squares = [x**2 for x in range(5)]
    print(f"Squares: {squares}")
    
    # Tuples - Ordered, immutable
    coordinates = (10, 20)
    x, y = coordinates  # Unpacking
    print(f"Tuple: {coordinates}, Unpacked: x={x}, y={y}")
    
    # Dictionaries - Key-value pairs
    person = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    person["email"] = "alice@example.com"
    print(f"Dictionary: {person}")
    print(f"Keys: {list(person.keys())}")
    print(f"Values: {list(person.values())}")
    
    # Sets - Unordered, no duplicates
    numbers = {1, 2, 3, 2, 4, 3}
    numbers.add(5)
    print(f"Set (no duplicates): {numbers}")
    print(f"Union: {numbers | {4,5,6}}")
    print(f"Intersection: {numbers & {2,3,7}}")

# ============================================
# 3. CONTROL FLOW
# ============================================

def control_flow():
    print("\n" + "=" * 50)
    print("3. CONTROL FLOW")
    print("=" * 50)
    
    # If-elif-else
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"Score: {score}, Grade: {grade}")
    
    # Ternary operator
    age = 18
    status = "Adult" if age >= 18 else "Minor"
    print(f"Age {age}: {status}")
    
    # For loops
    print("For loop:", end=" ")
    for i in range(5):
        print(i, end=" ")
    print()
    
    # While loop
    count = 3
    while count > 0:
        print(f"Countdown: {count}")
        count -= 1
    
    # Break and continue
    for i in range(5):
        if i == 2:
            continue
        if i == 4:
            break
        print(f"Loop: {i}", end=" ")
    print()

# ============================================
# 4. FUNCTIONS
# ============================================

def functions():
    print("\n" + "=" * 50)
    print("4. FUNCTIONS")
    print("=" * 50)
    
    # Basic function
    def greet(name):
        return f"Hello, {name}!"
    
    print(greet("Alice"))
    
    # Default arguments
    def power(base, exponent=2):
        return base ** exponent
    
    print(f"Square of 5: {power(5)}")
    print(f"Cube of 3: {power(3, 3)}")
    
    # Multiple return values
    def get_min_max(numbers):
        return min(numbers), max(numbers)
    
    nums = [3, 1, 4, 1, 5]
    min_val, max_val = get_min_max(nums)
    print(f"Min: {min_val}, Max: {max_val}")
    
    # *args and **kwargs
    def sum_all(*args):
        return sum(args)
    
    def print_info(**kwargs):
        for key, value in kwargs.items():
            print(f"  {key}: {value}")
    
    print(f"Sum of 1,2,3,4: {sum_all(1,2,3,4)}")
    print("Person info:")
    print_info(name="Bob", age=25, city="London")
    
    # Lambda functions
    square = lambda x: x ** 2
    print(f"Lambda square: {square(6)}")
    
    # Map and filter
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, numbers))
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Map (squares): {squared}")
    print(f"Filter (evens): {evens}")

# ============================================
# 5. STRING OPERATIONS
# ============================================

def string_operations():
    print("\n" + "=" * 50)
    print("5. STRING OPERATIONS")
    print("=" * 50)
    
    text = "  Python Programming  "
    
    # Basic operations
    print(f"Original: '{text}'")
    print(f"Strip: '{text.strip()}'")
    print(f"Upper: {text.upper().strip()}")
    print(f"Lower: {text.lower().strip()}")
    print(f"Replace: {text.strip().replace('Python', 'Java')}")
    
    # Splitting and joining
    words = text.strip().split()
    print(f"Split: {words}")
    print(f"Join: {'-'.join(words)}")
    
    # Slicing
    text = "Hello World"
    print(f"Original: {text}")
    print(f"First 5 chars: {text[:5]}")
    print(f"Last 5 chars: {text[-5:]}")
    print(f"Reverse: {text[::-1]}")
    
    # String formatting
    name = "Alice"
    age = 25
    print(f"F-string: {name} is {age} years old")
    print("Format: {} is {} years old".format(name, age))
    print("Concatenation: " + name + " is " + str(age))

# ============================================
# 6. FILE HANDLING
# ============================================

def file_handling():
    print("\n" + "=" * 50)
    print("6. FILE HANDLING")
    print("=" * 50)
    
    # Writing to file
    with open("sample.txt", "w") as file:
        file.write("Line 1\n")
        file.write("Line 2\n")
        file.write("Line 3\n")
    print("File written successfully")
    
    # Reading file
    with open("sample.txt", "r") as file:
        content = file.read()
        print(f"File content:\n{content}")
    
    # Reading line by line
    print("Reading line by line:")
    with open("sample.txt", "r") as file:
        for line in file:
            print(f"  {line.strip()}")
    
    # Appending to file
    with open("sample.txt", "a") as file:
        file.write("Line 4 (appended)\n")
    
    # Read all lines into list
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        print(f"Lines list: {lines}")
    
    # Clean up
    import os
    if os.path.exists("sample.txt"):
        os.remove("sample.txt")
        print("File deleted")

# ============================================
# 7. EXCEPTION HANDLING
# ============================================

def exception_handling():
    print("\n" + "=" * 50)
    print("7. EXCEPTION HANDLING")
    print("=" * 50)
    
    # Basic try-except
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Caught: Division by zero!")
    
    # Multiple exceptions
    try:
        num = int("not a number")
    except ValueError:
        print("Caught: Invalid conversion!")
    except ZeroDivisionError:
        print("This won't execute")
    
    # Try-except-else-finally
    try:
        num = int("123")
    except ValueError:
        print("Conversion failed")
    else:
        print(f"Conversion successful: {num}")
    finally:
        print("This always executes")
    
    # Raising exceptions
    def validate_age(age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        return age
    
    try:
        validate_age(-5)
    except ValueError as e:
        print(f"Validation error: {e}")

# ============================================
# 8. OBJECT-ORIENTED PROGRAMMING
# ============================================

def oop():
    print("\n" + "=" * 50)
    print("8. OBJECT-ORIENTED PROGRAMMING")
    print("=" * 50)
    
    # Class definition
    class Student:
        # Class variable
        school = "Python University"
        
        # Constructor
        def __init__(self, name, grade):
            self.name = name      # Instance variable
            self.grade = grade    # Instance variable
        
        # Method
        def display(self):
            return f"{self.name} has grade: {self.grade}"
        
        # Class method
        @classmethod
        def change_school(cls, new_school):
            cls.school = new_school
        
        # Static method
        @staticmethod
        def is_passing(grade):
            return grade >= 60
    
    # Creating objects
    student1 = Student("Alice", 85)
    student2 = Student("Bob", 55)
    
    print(student1.display())
    print(student2.display())
    print(f"School: {Student.school}")
    print(f"Is 85 passing? {Student.is_passing(85)}")
    
    # Inheritance
    class Animal:
        def __init__(self, name):
            self.name = name
        
        def speak(self):
            return "Some sound"
    
    class Dog(Animal):
        def speak(self):
            return f"{self.name} says Woof!"
    
    class Cat(Animal):
        def speak(self):
            return f"{self.name} says Meow!"
    
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    
    print(dog.speak())
    print(cat.speak())
    
    # Polymorphism
    animals = [dog, cat]
    for animal in animals:
        print(animal.speak())

# ============================================
# 9. COMMON MODULES
# ============================================

def common_modules():
    print("\n" + "=" * 50)
    print("9. COMMON MODULES")
    print("=" * 50)
    
    # datetime
    from datetime import datetime, timedelta
    now = datetime.now()
    print(f"Current time: {now}")
    print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    
    tomorrow = now + timedelta(days=1)
    print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")
    
    # math
    import math
    print(f"Pi: {math.pi}")
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"Factorial of 5: {math.factorial(5)}")
    
    # random
    import random
    print(f"Random number: {random.randint(1, 100)}")
    print(f"Random choice: {random.choice(['a', 'b', 'c'])}")
    
    # json
    import json
    data = {"name": "Alice", "age": 25}
    json_str = json.dumps(data)
    print(f"JSON string: {json_str}")
    print(f"Parsed JSON: {json.loads(json_str)}")
    
    # os
    import os
    print(f"Current directory: {os.getcwd()}")
    print(f"Files in directory: {len(os.listdir('.'))}")

# ============================================
# 10. BASIC ALGORITHMS
# ============================================

def basic_algorithms():
    print("\n" + "=" * 50)
    print("10. BASIC ALGORITHMS")
    print("=" * 50)
    
    # Linear Search
    def linear_search(arr, target):
        for i, val in enumerate(arr):
            if val == target:
                return i
        return -1
    
    arr = [3, 7, 1, 9, 4, 6]
    target = 9
    result = linear_search(arr, target)
    print(f"Linear Search: {target} found at index {result}")
    
    # Binary Search (sorted array)
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    sorted_arr = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    result = binary_search(sorted_arr, target)
    print(f"Binary Search: {target} found at index {result}")
    
    # Bubble Sort
    def bubble_sort(arr):
        arr = arr.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
    unsorted = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(unsorted)
    print(f"Bubble Sort: {unsorted} -> {sorted_arr}")
    
    # Factorial (recursion)
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n-1)
    
    print(f"Factorial of 5: {factorial(5)}")
    
    # Fibonacci
    def fibonacci(n):
        a, b = 0, 1
        result = []
        for _ in range(n):
            result.append(a)
            a, b = b, a + b
        return result
    
    print(f"First 10 Fibonacci: {fibonacci(10)}")

# ============================================
# 11. LIST COMPREHENSIONS & LAMBDA
# ============================================

def advanced_features():
    print("\n" + "=" * 50)
    print("11. ADVANCED FEATURES")
    print("=" * 50)
    
    # List comprehension with condition
    numbers = range(1, 11)
    even_squares = [x**2 for x in numbers if x % 2 == 0]
    print(f"Even squares: {even_squares}")
    
    # Dictionary comprehension
    squares_dict = {x: x**2 for x in range(5)}
    print(f"Dictionary squares: {squares_dict}")
    
    # Set comprehension
    unique_squares = {x**2 for x in [1, 2, 2, 3, 3, 3]}
    print(f"Set squares (unique): {unique_squares}")
    
    # Multiple iterators
    pairs = [(x, y) for x in range(3) for y in range(3)]
    print(f"Pairs: {pairs[:5]}...")  # First 5 pairs
    
    # zip and enumerate
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]
    
    for i, (name, score) in enumerate(zip(names, scores)):
        print(f"{i+1}. {name}: {score}")
    
    # Sorted with key
    students = [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 92},
        {"name": "Charlie", "grade": 78}
    ]
    sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)
    print(f"Top student: {sorted_students[0]['name']}")

# ============================================
# MAIN EXECUTION
# ============================================

def main():
    """Run all practice examples"""
    print("\n" + "="*60)
    print("PYTHON PRACTICE - COMPLETE EXAMPLES")
    print("="*60)
    
    basic_concepts()
    data_structures()
    control_flow()
    functions()
    string_operations()
    file_handling()
    exception_handling()
    oop()
    common_modules()
    basic_algorithms()
    advanced_features()
    
    print("\n" + "="*60)
    print("All examples completed successfully!")
    print("="*60)

if __name__ == "__main__":
    main()