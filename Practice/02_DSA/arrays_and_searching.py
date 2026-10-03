# ============================================================
# DSA - ARRAYS & SEARCHING PRACTICE
# Topic: Array operations, Linear Search, Binary Search
# Date: 2026-09-22
# ============================================================


# ----------------------------------------------------------
# 1. REVERSE AN ARRAY (without built-in reverse)
# ----------------------------------------------------------

print("=" * 50)
print("1. REVERSE AN ARRAY")
print("=" * 50)

arr = [10, 20, 30, 40, 50]
print("Original:", arr)

reversed_arr = []
for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])
print("Reversed:", reversed_arr)

# In-place reversal using two pointers
arr2 = [10, 20, 30, 40, 50]
left, right = 0, len(arr2) - 1
while left < right:
    arr2[left], arr2[right] = arr2[right], arr2[left]
    left += 1
    right -= 1
print("In-place reversed:", arr2)


# ----------------------------------------------------------
# 2. FIND SECOND LARGEST ELEMENT
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("2. SECOND LARGEST ELEMENT")
print("=" * 50)

arr = [12, 35, 1, 10, 34, 1]
print("Array:", arr)

first = second = float('-inf')
for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print(f"Largest: {first}, Second Largest: {second}")


# ----------------------------------------------------------
# 3. REMOVE DUPLICATES FROM SORTED ARRAY
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("3. REMOVE DUPLICATES")
print("=" * 50)

arr = [1, 1, 2, 2, 3, 4, 4, 5, 5, 5]
print("Original:", arr)

unique = [arr[0]]
for i in range(1, len(arr)):
    if arr[i] != arr[i - 1]:
        unique.append(arr[i])
print("After removing duplicates:", unique)


# ----------------------------------------------------------
# 4. ROTATE ARRAY BY K POSITIONS
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("4. ROTATE ARRAY")
print("=" * 50)

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(f"Original: {arr}, Rotate by: {k}")

k = k % len(arr)
rotated = arr[-k:] + arr[:-k]
print("After right rotation:", rotated)


# ----------------------------------------------------------
# 5. LINEAR SEARCH
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("5. LINEAR SEARCH")
print("=" * 50)


def linear_search(arr, target):
    """Search for target in arr, return index or -1."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [23, 45, 12, 67, 89, 34, 56]
target = 67
result = linear_search(arr, target)
print(f"Array: {arr}")
print(f"Searching for {target}: Found at index {result}")

target = 99
result = linear_search(arr, target)
print(f"Searching for {target}: {'Found at index ' + str(result) if result != -1 else 'Not Found'}")


# ----------------------------------------------------------
# 6. BINARY SEARCH
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("6. BINARY SEARCH")
print("=" * 50)


def binary_search(arr, target):
    """Binary search on sorted array. Returns index or -1."""
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


sorted_arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
result = binary_search(sorted_arr, target)
print(f"Sorted Array: {sorted_arr}")
print(f"Searching for {target}: Found at index {result}")

target = 50
result = binary_search(sorted_arr, target)
print(f"Searching for {target}: {'Found at index ' + str(result) if result != -1 else 'Not Found'}")


# ----------------------------------------------------------
# 7. FIND MISSING NUMBER (1 to N)
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("7. FIND MISSING NUMBER")
print("=" * 50)

arr = [1, 2, 4, 5, 6, 7, 8]
n = len(arr) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)
missing = expected_sum - actual_sum
print(f"Array: {arr}")
print(f"Missing number: {missing}")


# ----------------------------------------------------------
# 8. MAXIMUM SUBARRAY SUM (Kadane's Algorithm)
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("8. KADANE'S ALGORITHM")
print("=" * 50)


def kadanes_algorithm(arr):
    """Find maximum sum of contiguous subarray."""
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Array: {arr}")
print(f"Maximum subarray sum: {kadanes_algorithm(arr)}")


# ----------------------------------------------------------
# 9. TWO SUM PROBLEM
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("9. TWO SUM PROBLEM")
print("=" * 50)


def two_sum(arr, target):
    """Find two numbers that add up to target."""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None


arr = [2, 7, 11, 15]
target = 9
result = two_sum(arr, target)
print(f"Array: {arr}, Target: {target}")
if result:
    print(f"Indices: {result} → {arr[result[0]]} + {arr[result[1]]} = {target}")
