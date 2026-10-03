# numpy practice

import numpy as np

# creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
print("1d array:", arr1, "| shape:", arr1.shape, "| dtype:", arr1.dtype)

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2d array:\n", arr2, "\n  shape:", arr2.shape)

# different ways to create
print("\nzeros (2x3):\n", np.zeros((2, 3)))
print("ones (3x3):\n", np.ones((3, 3)))
print("identity (3x3):\n", np.eye(3))
print("arange (0-9):", np.arange(0, 10))
print("linspace (0-1, 5 pts):", np.linspace(0, 1, 5))
print("random (2x3):\n", np.random.rand(2, 3))


# indexing and slicing
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("\narray:", arr)
print("element at index 3:", arr[3])
print("last element:", arr[-1])
print("slice [2:6]:", arr[2:6])
print("every other element:", arr[::2])
print("reversed:", arr[::-1])

# 2d indexing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nmatrix:\n", matrix)
print("element [1,2]:", matrix[1, 2])
print("row 0:", matrix[0])
print("column 1:", matrix[:, 1])
print("sub-matrix [0:2, 1:3]:\n", matrix[0:2, 1:3])


# array operations
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print("\na:", a)
print("b:", b)
print("a + b:", a + b)
print("a * b:", a * b)
print("a ** 2:", a ** 2)
print("dot product:", np.dot(a, b))

# broadcasting
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\nmatrix:\n", matrix)
print("matrix + 10:\n", matrix + 10)
print("matrix * 2:\n", matrix * 2)


# statistics
marks = np.array([85, 72, 91, 68, 77, 95, 54, 81, 73, 88])
print("\nstudent marks:", marks)
print(f"  mean:   {marks.mean():.2f}")
print(f"  median: {np.median(marks):.2f}")
print(f"  std:    {marks.std():.2f}")
print(f"  min:    {marks.min()}")
print(f"  max:    {marks.max()}")
print(f"  sum:    {marks.sum()}")
print(f"  argmax: {marks.argmax()} (index of max)")
print(f"  argmin: {marks.argmin()} (index of min)")


# boolean indexing
print("\nmarks > 75:", marks[marks > 75])
print("marks < 70:", marks[marks < 70])
print("count of marks >= 80:", np.sum(marks >= 80))

# temperature analysis
temps = np.array([28, 31, 29, 33, 35, 27, 32])
days = np.array(["mon", "tue", "wed", "thu", "fri", "sat", "sun"])
print("\ntemperatures:", temps)
print("hot days (>30):", days[temps > 30])
print("avg temperature:", temps.mean())


# reshaping and stacking
arr = np.arange(1, 13)
print("\noriginal:", arr)
print("reshaped to 3x4:\n", arr.reshape(3, 4))
print("reshaped to 4x3:\n", arr.reshape(4, 3))
print("flattened:", arr.reshape(3, 4).flatten())

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("\nhorizontal stack:", np.hstack((a, b)))
print("vertical stack:\n", np.vstack((a, b)))
