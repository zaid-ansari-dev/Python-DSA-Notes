from array import *

array = [10, 20, 30, 40, 50]
print("Sub-Arrays")
print(array[1:4])
print(array[:3])
print(array[2:])


# pop() it mutates the og
array.pop()
print(array)
array.pop(2)
print(array)
x = array.pop(0)
print(x)
print(array)

array = [10, 20, 30, 40, 50]

# insert() shifts elements to right to make place
array.insert(2, 00)
y = array.insert(3, 91)  # pop returns what it removed insert return NOne
print(y)
print(array)

# append() only adds at last if you want specifics use insert(index,element)
z = array.append("hello")
print(z)
# return None
print(array)


# remove() removes the first occurence from index 0
array.append(0)
print(array)
array.remove(0)
print(array)
# if you need to remove all the occurences you did do
array.insert(1, 'hello')
print(array)
# this is a list comprehension in python creates a temp list
array = [x for x in array if x != 'hello']
print(array)


# sort()
array.sort()
print(array)
array.sort(reverse=True)
print(array)
# also custom by string length
tempArr = ['a', 'dddd', 'bb', 'ccc']
tempArr.sort(key=len)
print(tempArr)

# sorted -- creates a temp list | does not mutate the og
arr = [3, 1, 2]
a = sorted(arr)
print(a)

# reverse no-condition
arr.reverse()
print(arr)
