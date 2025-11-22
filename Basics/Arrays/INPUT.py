from array import *

arr = array("i", [])
n = int(input("Enter the limit for the array: "))

for i in range(n):
    x = int(input("Enter the array: "))
    arr.append(x)

print(arr)


val = int(input("Enter the values to search: "))

k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k += 1

print("now the function--")
print(arr.index(val))
