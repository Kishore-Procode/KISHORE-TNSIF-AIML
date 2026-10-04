"""
Data Structure Questions Assignment
"""

# 1. Two Sum - Hashing
def two_sum(nums, target):
    """
    Given an integer array and a target value, find the indices of two elements whose sum equals the target.
    Example: [2, 7, 11, 15], target = 9 -> [0, 1]
    """
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

# 2. Longest Substring Without Repeating Characters - Sliding Window
def length_of_longest_substring(s: str) -> int:
    """
    Given a string, find the length of the longest substring containing no duplicate characters.
    Example: "abcabcbb" -> 3
    """
    char_map = {}
    left = 0
    max_len = 0
    for right in range(len(s)):
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
        char_map[s[right]] = right
        max_len = max(max_len, right - left + 1)
    return max_len

# 3. Maximum Subarray Sum - Kadane's Algorithm
def max_sub_array(nums):
    """
    Find the contiguous subarray having the maximum possible sum.
    Example: [-2,1,-3,4,-1,2,1,-5,4] -> 6
    """
    if not nums:
        return 0
    current_max = global_max = nums[0]
    for num in nums[1:]:
        current_max = max(num, current_max + num)
        global_max = max(global_max, current_max)
    return global_max

# 4. Merge Overlapping Intervals - Sorting
def merge_intervals(intervals):
    """
    Given a collection of intervals, merge all overlapping intervals.
    Example: [[1,3],[2,6],[8,10],[9,12]] -> [[1,6],[8,12]]
    """
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last_merged = merged[-1]
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)
    return merged

# 5. Detect a Cycle in a Linked List - Fast & Slow Pointers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: ListNode) -> bool:
    """
    Determine whether a singly linked list contains a cycle. O(1) extra space.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# 6. Valid Parentheses - Stack
def is_valid_parentheses(s: str) -> bool:
    """
    Given a string containing (), {}, and [], determine whether the brackets are properly balanced.
    Example: "({[]})" -> true
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

# 7. Binary Tree Level Order Traversal - BFS
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root: TreeNode):
    """
    Given the root of a binary tree, return its nodes level by level.
    """
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(current_level)
    return result

# 8. Lowest Common Ancestor of a Binary Tree
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Given a binary tree and two nodes p and q, find their lowest common ancestor.
    """
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right

# 9. Number of Islands - Graph/BFS/DFS
def num_islands(grid):
    """
    Given a grid containing '1' (land) and '0' (water), count the number of distinct islands.
    """
    if not grid:
        return 0
    count = 0
    rows, cols = len(grid), len(grid[0])
    
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0' # mark as visited
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count

# 10. Longest Consecutive Sequence - Hashing
def longest_consecutive(nums):
    """
    Given an unsorted array, find the length of the longest sequence of consecutive integers.
    Example: [100,4,200,1,3,2] -> 4 (1,2,3,4)
    """
    num_set = set(nums)
    longest_streak = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak


if __name__ == "__main__":
    # Test cases
    print("1. Two Sum:", two_sum([2, 7, 11, 15], 9))
    print("2. Longest Substring:", length_of_longest_substring("abcabcbb"))
    print("3. Max Subarray:", max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
    print("4. Merge Intervals:", merge_intervals([[1,3],[2,6],[8,10],[9,12]]))
    print("6. Valid Parentheses:", is_valid_parentheses("({[]})"))
    print("9. Num Islands:", num_islands([
        ['1','1','0','0'],
        ['1','0','0','1'],
        ['0','0','1','1']
    ]))
    print("10. Longest Consecutive:", longest_consecutive([100,4,200,1,3,2]))
