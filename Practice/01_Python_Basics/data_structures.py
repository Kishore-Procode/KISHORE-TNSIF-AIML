# data structures practice - lists, tuples, sets, dictionaries

# lists
fruits = ["apple", "banana", "cherry", "mango", "grape"]
print("original list:", fruits)

print("first fruit:", fruits[0])
print("last fruit:", fruits[-1])
print("slicing [1:3]:", fruits[1:3])

fruits.append("orange")
print("after append:", fruits)

fruits.insert(2, "kiwi")
print("after insert at index 2:", fruits)

fruits.remove("banana")
print("after removing banana:", fruits)

popped = fruits.pop()
print(f"popped: {popped}, list now: {fruits}")

# list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x ** 2 for x in numbers]
print("\nnumbers:", numbers)
print("squares:", squares)

evens = [x for x in numbers if x % 2 == 0]
print("even numbers:", evens)

# sorting
unsorted = [64, 25, 12, 22, 11]
print("\nunsorted:", unsorted)
print("sorted (asc):", sorted(unsorted))
print("sorted (desc):", sorted(unsorted, reverse=True))


# tuples
coordinates = (10, 20, 30)
print("\ncoordinates:", coordinates)
print("x:", coordinates[0], "y:", coordinates[1], "z:", coordinates[2])

# unpacking
x, y, z = coordinates
print(f"unpacked -> x={x}, y={y}, z={z}")

print("count of 10:", coordinates.count(10))
print("index of 20:", coordinates.index(20))
print("length:", len(coordinates))

# nested tuples
students = (
    ("Kishore", 85),
    ("Arun", 90),
    ("Bala", 78)
)
print("\nstudent records:")
for name, marks in students:
    print(f"  {name}: {marks}")


# sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("\nset a:", set_a)
print("set b:", set_b)
print("union:", set_a | set_b)
print("intersection:", set_a & set_b)
print("difference (a-b):", set_a - set_b)
print("symmetric difference:", set_a ^ set_b)

# removing duplicates using set
nums_with_dupes = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_nums = list(set(nums_with_dupes))
print("\nwith duplicates:", nums_with_dupes)
print("without duplicates:", unique_nums)


# dictionaries
student = {
    "name": "Kishore",
    "age": 21,
    "department": "CSE",
    "marks": {"math": 90, "physics": 85, "chemistry": 88}
}

print("\nstudent:", student)
print("name:", student["name"])
print("math marks:", student["marks"]["math"])

student["year"] = 3
student["age"] = 22
print("after update:", student)

print("\nall keys:", list(student.keys()))
print("all values:", list(student.values()))

print("\niterating:")
for key, value in student.items():
    print(f"  {key}: {value}")

# word frequency counter
sentence = "python is great and python is fun and python is easy"
words = sentence.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print("\nword frequency:")
for word, count in frequency.items():
    print(f"  '{word}': {count}")
