from array import *

arr = array("i", [])
n = int(input("Enter the limit: "))

for i in range(n):
    x = int(input("Enter the array: "))
    arr.append(x)

print(arr)

print("what index to remove")
index = int(input("Enter here: "))

for i in range(index, len(arr) - 1):
    arr[i] = arr[i+1]

arr = arr[:-1]

print(arr)

print("now Reverse array")

arr = arr[::-1]
print(arr)
