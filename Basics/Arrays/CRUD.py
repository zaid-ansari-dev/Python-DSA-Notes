# import array as arr

# you would need to use

# arr.array()

from array import *

values = array("i", [1, -2, 3, 4])
print(values)
print(values.buffer_info())
print(values.typecode)
print(values.reverse())  # None
print(values.append(5))  # None cuz it does not return anything
print(values[0])

# to print array
print(*values)
for val in values:
    print(val, end=" ")

print("\n")
print(values.tolist())

for val in range(len(values)):
    print(val)  # this will print indices
    print("break")
    print(values[val])


char = array("w", ["a", "b", "c"])  # u is deprecated use 'w'
for ch in char:
    print(ch)

print("breakpoint")

newChar = array(char.typecode, (a for a in char))  # copy the above array
for ch in newChar:
    print(ch)

print('break')

newValues = array(values.typecode, (a*a for a in values))  # copy and sq
for val in newValues:
    print(val)

print("breakpoint")

#   using while loop
newArr = array(values.typecode, (a for a in values))
i = 0
while i < len(newArr):
    print(newArr[i])
    i += 1
