# ============================================================
# PYTHON FUNDAMENTALS - PRACTICE
# Topic: Variables, Data Types, Operators, Conditionals, Loops
# Date: 2026-09-15
# ============================================================


# ----------------------------------------------------------
# 1. VARIABLES & DATA TYPES
# ----------------------------------------------------------

name = "Kishore"
age = 21
height = 5.9
is_student = True

print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Is Student:", is_student, "| Type:", type(is_student))


# ----------------------------------------------------------
# 2. ARITHMETIC OPERATORS
# ----------------------------------------------------------

a, b = 15, 4

print("\n--- Arithmetic Operators ---")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")


# ----------------------------------------------------------
# 3. CONDITIONAL STATEMENTS
# ----------------------------------------------------------

# Check if a number is even or odd
num = 17
print("\n--- Conditionals ---")
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# Find the largest of three numbers
x, y, z = 45, 78, 32
if x > y and x > z:
    print(f"Largest: {x}")
elif y > x and y > z:
    print(f"Largest: {y}")
else:
    print(f"Largest: {z}")

# Grade calculator
marks = 82
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"
print(f"Marks: {marks} → Grade: {grade}")


# ----------------------------------------------------------
# 4. LOOPS - FOR LOOP
# ----------------------------------------------------------

print("\n--- For Loops ---")

# Print numbers 1 to 10
print("Numbers 1 to 10:", end=" ")
for i in range(1, 11):
    print(i, end=" ")
print()

# Sum of first N natural numbers
n = 20
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of 1 to {n}: {total}")

# Multiplication table
num = 7
print(f"\nMultiplication table of {num}:")
for i in range(1, 11):
    print(f"  {num} × {i} = {num * i}")

# Count even numbers in a range
n = 50
even_count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_count += 1
print(f"\nEven numbers from 1 to {n}: {even_count}")


# ----------------------------------------------------------
# 5. LOOPS - WHILE LOOP
# ----------------------------------------------------------

print("\n--- While Loops ---")

# Factorial of a number
num = 6
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print(f"Factorial of {num}: {factorial}")

# Reverse a number
original = 12345
reversed_num = 0
temp = original
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
print(f"Reverse of {original}: {reversed_num}")

# Sum of digits
num = 9876
digit_sum = 0
temp = num
while temp > 0:
    digit_sum += temp % 10
    temp //= 10
print(f"Sum of digits of {num}: {digit_sum}")


# ----------------------------------------------------------
# 6. PRIME NUMBER CHECK
# ----------------------------------------------------------

print("\n--- Prime Number Check ---")
num = 29
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
print(f"{num} is {'Prime' if is_prime else 'Not Prime'}")


# ----------------------------------------------------------
# 7. PATTERN PRINTING
# ----------------------------------------------------------

print("\n--- Star Pattern ---")
rows = 5
for i in range(1, rows + 1):
    print("* " * i)

print("\n--- Number Triangle ---")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# ----------------------------------------------------------
# 8. FUNCTIONS
# ----------------------------------------------------------

print("\n--- Functions ---")


def is_palindrome(num):
    """Check if a number is a palindrome."""
    original = num
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return original == reversed_num


def fibonacci(n):
    """Generate fibonacci series up to n terms."""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


print(f"121 is palindrome: {is_palindrome(121)}")
print(f"123 is palindrome: {is_palindrome(123)}")
print(f"Fibonacci (10 terms): {fibonacci(10)}")


# ----------------------------------------------------------
# 9. STRING OPERATIONS
# ----------------------------------------------------------

print("\n--- String Operations ---")
text = "Hello, Python!"

print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Length: {len(text)}")
print(f"Reversed: {text[::-1]}")
print(f"Word count: {len(text.split())}")
print(f"Replace: {text.replace('Python', 'World')}")

# Count vowels
vowels = sum(1 for ch in text.lower() if ch in 'aeiou')
print(f"Vowel count: {vowels}")
