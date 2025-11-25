from array import *
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
for row in matrix:
    print(row)

for row in matrix:
    for x in row:
        print(x, end=" ")

# now easy approach with list comprehension
print("checkout")
flat = [x for row in matrix for x in row]
print(flat)
