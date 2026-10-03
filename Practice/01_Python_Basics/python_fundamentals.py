# python basics practice - variables, loops, conditionals, functions

# variables and types
name = "Kishore"
age = 21
height = 5.9
is_student = True

print("name:", name, "| type:", type(name))
print("age:", age, "| type:", type(age))
print("height:", height, "| type:", type(height))
print("is student:", is_student, "| type:", type(is_student))


# arithmetic operators
a, b = 15, 4

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")


# even or odd check
num = 17
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# largest of three
x, y, z = 45, 78, 32
if x > y and x > z:
    print(f"largest: {x}")
elif y > x and y > z:
    print(f"largest: {y}")
else:
    print(f"largest: {z}")

# grade calculator
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
print(f"marks: {marks} -> grade: {grade}")


# for loops

# print 1 to 10
print("numbers 1 to 10:", end=" ")
for i in range(1, 11):
    print(i, end=" ")
print()

# sum of first n numbers
n = 20
total = 0
for i in range(1, n + 1):
    total += i
print(f"sum of 1 to {n}: {total}")

# multiplication table
num = 7
print(f"\nmultiplication table of {num}:")
for i in range(1, 11):
    print(f"  {num} x {i} = {num * i}")

# count even numbers
n = 50
even_count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_count += 1
print(f"\neven numbers from 1 to {n}: {even_count}")


# while loops

# factorial
num = 6
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print(f"factorial of {num}: {factorial}")

# reverse a number
original = 12345
reversed_num = 0
temp = original
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
print(f"reverse of {original}: {reversed_num}")

# sum of digits
num = 9876
digit_sum = 0
temp = num
while temp > 0:
    digit_sum += temp % 10
    temp //= 10
print(f"sum of digits of {num}: {digit_sum}")


# prime check
num = 29
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
print(f"{num} is {'prime' if is_prime else 'not prime'}")


# pattern printing
rows = 5
for i in range(1, rows + 1):
    print("* " * i)

print()
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# functions

def is_palindrome(num):
    original = num
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return original == reversed_num

def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print(f"121 is palindrome: {is_palindrome(121)}")
print(f"123 is palindrome: {is_palindrome(123)}")
print(f"fibonacci (10 terms): {fibonacci(10)}")


# string operations
text = "Hello, Python!"

print(f"original: {text}")
print(f"uppercase: {text.upper()}")
print(f"lowercase: {text.lower()}")
print(f"length: {len(text)}")
print(f"reversed: {text[::-1]}")
print(f"word count: {len(text.split())}")
print(f"replace: {text.replace('Python', 'World')}")

# count vowels
vowels = sum(1 for ch in text.lower() if ch in 'aeiou')
print(f"vowel count: {vowels}")
