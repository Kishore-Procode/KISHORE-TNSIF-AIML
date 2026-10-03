# sorting algorithms practice

# bubble sort
def bubble_sort(arr):
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
print("original:", data.copy())
print("bubble sorted:", bubble_sort(data))


# selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

data = [29, 10, 14, 37, 13]
print("\noriginal:", data.copy())
print("selection sorted:", selection_sort(data))


# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

data = [12, 11, 13, 5, 6]
print("\noriginal:", data.copy())
print("insertion sorted:", insertion_sort(data))


# comparing all three with same data
import time

test_data = [38, 27, 43, 3, 9, 82, 10, 55, 33, 21,
             15, 44, 62, 7, 91, 28, 50, 17, 36, 70]

data_copy = test_data.copy()
start = time.time()
bubble_sort(data_copy)
bubble_time = time.time() - start
print(f"\nbubble sort time: {bubble_time:.6f}s")

data_copy = test_data.copy()
start = time.time()
selection_sort(data_copy)
selection_time = time.time() - start
print(f"selection sort time: {selection_time:.6f}s")

data_copy = test_data.copy()
start = time.time()
insertion_sort(data_copy)
insertion_time = time.time() - start
print(f"insertion sort time: {insertion_time:.6f}s")

# time complexities
# bubble sort    -> best O(n), worst O(n^2), space O(1)
# selection sort -> best O(n^2), worst O(n^2), space O(1)
# insertion sort -> best O(n), worst O(n^2), space O(1)
