# ============================================================
# NUMPY PRACTICE
# Topic: Array operations, Indexing, Math, Statistics
# Date: 2026-09-26
# ============================================================

import numpy as np


# ----------------------------------------------------------
# 1. ARRAY CREATION
# ----------------------------------------------------------

print("=" * 50)
print("1. ARRAY CREATION")
print("=" * 50)

# Different ways to create arrays
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1, "| Shape:", arr1.shape, "| Dtype:", arr1.dtype)

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:\n", arr2, "\n  Shape:", arr2.shape)

# Special arrays
print("\nZeros (2x3):\n", np.zeros((2, 3)))
print("Ones (3x3):\n", np.ones((3, 3)))
print("Identity (3x3):\n", np.eye(3))
print("Arange (0-9):", np.arange(0, 10))
print("Linspace (0-1, 5 pts):", np.linspace(0, 1, 5))
print("Random (2x3):\n", np.random.rand(2, 3))


# ----------------------------------------------------------
# 2. ARRAY INDEXING & SLICING
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("2. INDEXING & SLICING")
print("=" * 50)

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Array:", arr)
print("Element at index 3:", arr[3])
print("Last element:", arr[-1])
print("Slice [2:6]:", arr[2:6])
print("Every other element:", arr[::2])
print("Reversed:", arr[::-1])

# 2D indexing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nMatrix:\n", matrix)
print("Element [1,2]:", matrix[1, 2])
print("Row 0:", matrix[0])
print("Column 1:", matrix[:, 1])
print("Sub-matrix [0:2, 1:3]:\n", matrix[0:2, 1:3])


# ----------------------------------------------------------
# 3. ARRAY OPERATIONS
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("3. ARRAY OPERATIONS")
print("=" * 50)

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print("a:", a)
print("b:", b)
print("a + b:", a + b)
print("a * b:", a * b)
print("a ** 2:", a ** 2)
print("Dot product:", np.dot(a, b))

# Broadcasting
matrix = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10
print("\nMatrix:\n", matrix)
print("Matrix + 10:\n", matrix + scalar)
print("Matrix * 2:\n", matrix * 2)


# ----------------------------------------------------------
# 4. STATISTICAL OPERATIONS
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("4. STATISTICS")
print("=" * 50)

marks = np.array([85, 72, 91, 68, 77, 95, 54, 81, 73, 88])
print("Student Marks:", marks)
print(f"  Mean:   {marks.mean():.2f}")
print(f"  Median: {np.median(marks):.2f}")
print(f"  Std:    {marks.std():.2f}")
print(f"  Min:    {marks.min()}")
print(f"  Max:    {marks.max()}")
print(f"  Sum:    {marks.sum()}")
print(f"  Argmax: {marks.argmax()} (index of max)")
print(f"  Argmin: {marks.argmin()} (index of min)")


# ----------------------------------------------------------
# 5. BOOLEAN INDEXING & FILTERING
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("5. BOOLEAN INDEXING")
print("=" * 50)

print("Marks > 75:", marks[marks > 75])
print("Marks < 70:", marks[marks < 70])
print("Count of marks >= 80:", np.sum(marks >= 80))

# Temperature analysis
temps = np.array([28, 31, 29, 33, 35, 27, 32])
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
print("\nTemperatures:", temps)
print("Hot days (>30°C):", days[temps > 30])
print("Avg temperature:", temps.mean())


# ----------------------------------------------------------
# 6. RESHAPING & STACKING
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("6. RESHAPING & STACKING")
print("=" * 50)

arr = np.arange(1, 13)
print("Original:", arr)
print("Reshaped to 3x4:\n", arr.reshape(3, 4))
print("Reshaped to 4x3:\n", arr.reshape(4, 3))
print("Flattened:", arr.reshape(3, 4).flatten())

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("\nHorizontal stack:", np.hstack((a, b)))
print("Vertical stack:\n", np.vstack((a, b)))
