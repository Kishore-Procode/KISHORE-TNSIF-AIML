# Qn: Write a Python program to take a number as input and check whether it is even or odd.

# x = int(input("value :"))
# if x%2 == 0 :
#     print("it is even")
# else :
#     print("it is odd")

# Qn: Write a Python program to take three numbers as input and print the largest number.

# a = int(input("No 1 :"))
# b = int(input("No 2 :"))
# c = int(input("No 3 :"))
# if a > b and a > c :
#     print("a is largest")
# elif b> a and b > c :
#     print("b is largest")
# else :
#     print("c is largest")

# Qn: Write a Python program to take a number n as input and print all numbers from 1 to n.

#n = int(input("range :"))
#for n in range(1,n+1):
#    print(n)


#Qn: Write a Python program to take a number n as input and print the sum of all numbers from 1 to n.

#n = int(input("value : "))
#i = 1
#for k in range(2,n+1):
#    i = i + k
#print(i)

#Qn: Write a Python program to take a number n as input and print the multiplication table of n from 1 to 10

#n = int(input("value : "))
#for i in range(1,11):
#        print( n , "*" , i , "=" , n*i)

#Qn: Write a Python program to take a number n as input and print all the even numbers from 1 to n.

#n = int(input("value : "))
#for i in range(1,n+1):
#    if i%2==0:
#        print(i)

#Write a Python program to take a number n as input and print the count of even numbers from 1 to n.

#n = int(input("value : "))
#k = 0
#for i in range(1,n+1):
#    if i%2==0:
#        k = k+1
#print(k)

#Qn: Write a Python program to take a number n as input and print the factorial of n.

#n = int(input("value : "))
#k = 1
#for i in range(1,n+1):
#    k = k * i
#print(k)


#Qn: Write a Python program to take a number n as input and check whether it is a prime number.

'''n = int(input("value : "))
for i in range(2,n):
    if n%i == 0:
        print(False)
        break
else:
    print(True)'''

#Qn: Write a Python program to take a number n as input and reverse the number.

num = int(input("Enter a number: "))
rev_number = 0
while num >= 0:
    digit = num%10
    rev_number = rev_number*10 + digit
    num = num//10
print(rev_number,num)






























    

