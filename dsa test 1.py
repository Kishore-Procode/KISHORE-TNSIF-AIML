import array

a = array.array('i',[1,2,3,4])

'''max1 = a[0]

for i in range(1, len(a)):
    if a[i] > max1:
        max1+=1
max1-=1
print("2nd largest No",max1)'''

#find the 2nd largest no
#find an element in an array

n = int(input("value "))

for i in range(len(a)):
    if a[i] == n:
        print(i)

