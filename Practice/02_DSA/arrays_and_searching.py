# arrays and searching practice

# reverse an array without built-in
arr = [10, 20, 30, 40, 50]
print("original:", arr)

reversed_arr = []
for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])
print("reversed:", reversed_arr)

# tried two pointer approach too
arr2 = [10, 20, 30, 40, 50]
left, right = 0, len(arr2) - 1
while left < right:
    arr2[left], arr2[right] = arr2[right], arr2[left]
    left += 1
    right -= 1
print("in-place reversed:", arr2)


# second largest element
arr = [12, 35, 1, 10, 34, 1]
print("\narray:", arr)

first = second = float('-inf')
for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print(f"largest: {first}, second largest: {second}")


# remove duplicates from sorted array
arr = [1, 1, 2, 2, 3, 4, 4, 5, 5, 5]
print("\noriginal:", arr)

unique = [arr[0]]
for i in range(1, len(arr)):
    if arr[i] != arr[i - 1]:
        unique.append(arr[i])
print("after removing duplicates:", unique)


# rotate array by k positions
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(f"\noriginal: {arr}, rotate by: {k}")

k = k % len(arr)
rotated = arr[-k:] + arr[:-k]
print("after right rotation:", rotated)


# linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [23, 45, 12, 67, 89, 34, 56]
target = 67
result = linear_search(arr, target)
print(f"\narray: {arr}")
print(f"searching for {target}: found at index {result}")

target = 99
result = linear_search(arr, target)
if result != -1:
    print(f"searching for {target}: found at index {result}")
else:
    print(f"searching for {target}: not found")


# binary search
def binary_search(arr, target):
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
print(f"\nsorted array: {sorted_arr}")
print(f"searching for {target}: found at index {result}")

target = 50
result = binary_search(sorted_arr, target)
if result != -1:
    print(f"searching for {target}: found at index {result}")
else:
    print(f"searching for {target}: not found")


# find missing number (1 to n)
arr = [1, 2, 4, 5, 6, 7, 8]
n = len(arr) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)
missing = expected_sum - actual_sum
print(f"\narray: {arr}")
print(f"missing number: {missing}")


# kadane's algorithm - max subarray sum
def kadanes_algorithm(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"\narray: {arr}")
print(f"maximum subarray sum: {kadanes_algorithm(arr)}")


# two sum problem
def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None

arr = [2, 7, 11, 15]
target = 9
result = two_sum(arr, target)
print(f"\narray: {arr}, target: {target}")
if result:
    print(f"indices: {result} -> {arr[result[0]]} + {arr[result[1]]} = {target}")
