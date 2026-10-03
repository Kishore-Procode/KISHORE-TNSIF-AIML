# ============================================================
# DSA - SORTING ALGORITHMS PRACTICE
# Topic: Bubble Sort, Selection Sort, Insertion Sort
# Date: 2026-09-24
# ============================================================


# ----------------------------------------------------------
# 1. BUBBLE SORT
# ----------------------------------------------------------

print("=" * 50)
print("1. BUBBLE SORT")
print("=" * 50)


def bubble_sort(arr):
    """Sort array using bubble sort algorithm."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


data = [64, 34, 25, 12, 22, 11, 90]
print("Original:", data.copy())
print("Sorted:  ", bubble_sort(data))


# ----------------------------------------------------------
# 2. SELECTION SORT
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("2. SELECTION SORT")
print("=" * 50)


def selection_sort(arr):
    """Sort array using selection sort algorithm."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


data = [29, 10, 14, 37, 13]
print("Original:", data.copy())
print("Sorted:  ", selection_sort(data))


# ----------------------------------------------------------
# 3. INSERTION SORT
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("3. INSERTION SORT")
print("=" * 50)


def insertion_sort(arr):
    """Sort array using insertion sort algorithm."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


data = [12, 11, 13, 5, 6]
print("Original:", data.copy())
print("Sorted:  ", insertion_sort(data))


# ----------------------------------------------------------
# 4. COMPARING ALL THREE SORTS
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("4. COMPARISON WITH SAME DATA")
print("=" * 50)

import time

test_data = [38, 27, 43, 3, 9, 82, 10, 55, 33, 21,
             15, 44, 62, 7, 91, 28, 50, 17, 36, 70]

# Bubble Sort timing
data_copy = test_data.copy()
start = time.time()
bubble_sort(data_copy)
bubble_time = time.time() - start
print(f"Bubble Sort:    {data_copy}  Time: {bubble_time:.6f}s")

# Selection Sort timing
data_copy = test_data.copy()
start = time.time()
selection_sort(data_copy)
selection_time = time.time() - start
print(f"Selection Sort: {data_copy}  Time: {selection_time:.6f}s")

# Insertion Sort timing
data_copy = test_data.copy()
start = time.time()
insertion_sort(data_copy)
insertion_time = time.time() - start
print(f"Insertion Sort: {data_copy}  Time: {insertion_time:.6f}s")

print("\n--- Time Complexities ---")
print("Bubble Sort:    Best O(n), Worst O(n²), Space O(1)")
print("Selection Sort: Best O(n²), Worst O(n²), Space O(1)")
print("Insertion Sort: Best O(n), Worst O(n²), Space O(1)")
