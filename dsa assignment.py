#1. Reverse an Array
#Write a program to reverse the elements of an array without using a built-in reverse function.

import array as arr

num = [1,2,3,4]

num1 = []
for i in range(len(num)):
    num1.append(num[-(i+1)])
print(num1)

#2. Count Even, Odd and Zero
#Write a program to count the number of even numbers, odd numbers, and zeros in an array.

num = [1,2,3,4,5,6,7]

count_even = 0
count_odd = 0
count_zero = 0

for i in range(len(num)):
    if num[i]%2==0:
        count_even +=1
    elif num[i]%2 != 0:
        count_odd +=1
    elif num[i] == 0:
        count_zero +=1

print("even : ",count_even,"\nodd : ",count_odd,"\nzero : ",count_zero)

#3. Sum of Positive and Negative Numbers
#Write a program to find the separate sum of positive and negative numbers in an array.

num = [1,2,-1,-4]

negative = 0
positive = 0

for i in range(len(num)):
    if num[i] <0:
        negative+=num[i]
    else:
        positive+=num[i]

print("positive sum :",positive,"\nnegative sum :",negative)

#4. Remove Duplicate Elements
#Write a program to remove duplicate elements from an array.



num = [1,2,3,4,5,3,4]
num1 = []

for i in range(len(num)):
    if num[i] not in num1:
        num1.append(num[i])
print(num1)

#5. Find the Missing Number
#An array contains numbers from 1 to N, but one number is missing. Find the missing number.

num = [1,2,3,4,6]
num1 = 0

for i in range(len(num)):
    num1+=num[i+1]
num1 = num1/len(num)

print(num1)
        
        



































       












