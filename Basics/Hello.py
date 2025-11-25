import math  # using lib of maths module
student = 1000
print(student)
float = 3.4
is_done = True
string = "hello"
course = """
    python prog.
"""
message = "hello"
print(len(message))
print(message[0])
print(message[-1])
print(message[0:3])
print(message[0:])
print(message[:3])
print(message[:])

talent = "python \" \\ \nProgramming"
print(talent)

# comments in python like // in js

first = "zaid"
last = "ansari"
full = first + " " + last
print(full)
newFull = f"{first} {last}"
print(newFull)
alsoFull = F"{first} {last}"
print(alsoFull)
expFull = F"{len(first)} {2+2} {last}"
print(expFull)

# string methods
animal = "  Python  "
print(animal.upper())
print(animal)
# other methods are:
# lower,title,strip
print(animal.strip())
print(animal.rstrip())

counting = "Python"
print(counting.find("y"))  # -1 means not found
print(animal.replace("P", "J"))
print(animal)
# differnce between 'in' and 'find' is that 'find' returns an index while 'in' returns a boolean value
print("Py" in animal)
print("un" not in animal)


# complex no.
x = 2
x = 3
x = 1 + 2j
print(10 + 2)
print(10 - 2)
print(10 * 2)
print(10 / 2)
print(10 // 2)
print(10 % 2)
print(10 ** 2)

x = 20
x = x + 3
x += 3
