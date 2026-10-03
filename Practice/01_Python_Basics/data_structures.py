# ============================================================
# DATA STRUCTURES IN PYTHON - PRACTICE
# Topic: Lists, Tuples, Sets, Dictionaries
# Date: 2026-09-18
# ============================================================


# ----------------------------------------------------------
# 1. LISTS
# ----------------------------------------------------------

print("=" * 50)
print("LISTS")
print("=" * 50)

# Creating and manipulating lists
fruits = ["apple", "banana", "cherry", "mango", "grape"]
print("Original list:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Slicing [1:3]:", fruits[1:3])

# List operations
fruits.append("orange")
print("After append:", fruits)

fruits.insert(2, "kiwi")
print("After insert at index 2:", fruits)

fruits.remove("banana")
print("After removing 'banana':", fruits)

popped = fruits.pop()
print(f"Popped: {popped}, List now: {fruits}")

# List comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x ** 2 for x in numbers]
print("\nNumbers:", numbers)
print("Squares:", squares)

evens = [x for x in numbers if x % 2 == 0]
print("Even numbers:", evens)

# Sorting
unsorted = [64, 25, 12, 22, 11]
print("\nUnsorted:", unsorted)
print("Sorted (asc):", sorted(unsorted))
print("Sorted (desc):", sorted(unsorted, reverse=True))


# ----------------------------------------------------------
# 2. TUPLES
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("TUPLES")
print("=" * 50)

# Creating tuples
coordinates = (10, 20, 30)
print("Coordinates:", coordinates)
print("X:", coordinates[0], "Y:", coordinates[1], "Z:", coordinates[2])

# Tuple unpacking
x, y, z = coordinates
print(f"Unpacked → x={x}, y={y}, z={z}")

# Tuple operations
print("Count of 10:", coordinates.count(10))
print("Index of 20:", coordinates.index(20))
print("Length:", len(coordinates))

# Nested tuples
students = (
    ("Kishore", 85),
    ("Arun", 90),
    ("Bala", 78)
)
print("\nStudent records:")
for name, marks in students:
    print(f"  {name}: {marks}")


# ----------------------------------------------------------
# 3. SETS
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("SETS")
print("=" * 50)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Set A:", set_a)
print("Set B:", set_b)
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A-B):", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)

# Removing duplicates from a list using sets
nums_with_dupes = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_nums = list(set(nums_with_dupes))
print("\nWith duplicates:", nums_with_dupes)
print("Without duplicates:", unique_nums)


# ----------------------------------------------------------
# 4. DICTIONARIES
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("DICTIONARIES")
print("=" * 50)

student = {
    "name": "Kishore",
    "age": 21,
    "department": "CSE",
    "marks": {"math": 90, "physics": 85, "chemistry": 88}
}

print("Student:", student)
print("Name:", student["name"])
print("Math marks:", student["marks"]["math"])

# Adding and updating
student["year"] = 3
student["age"] = 22
print("After update:", student)

# Iterating
print("\nAll keys:", list(student.keys()))
print("All values:", list(student.values()))

print("\nIterating:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Word frequency counter
sentence = "python is great and python is fun and python is easy"
words = sentence.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print("\nWord frequency:")
for word, count in frequency.items():
    print(f"  '{word}': {count}")
