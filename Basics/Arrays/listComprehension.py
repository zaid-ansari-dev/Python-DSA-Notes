from array import *

array = [1, 2, 3, 4, 5]
sq = [x*x for x in array]
print(sq)
fc = [x*x for x in array if x % 2 == 0]
print(fc)

fruits = ["apple", "banana", "kiwi", "pear"]
small = [x.upper() for x in fruits if len(x) <= 4]
print(small)

# nested loops work in one line
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [x for row in matrix for x in row]
print(flat)
