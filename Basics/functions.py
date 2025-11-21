# perform a task typa Function
def greet(first, last):
    print('this is a function in python')
    print(f"first_name: {first} and last_name: {last}")


greet("zaid", "ansari")
# this will return None as it is the default return value it got nothign to return it is not false (absence of a value)
print(greet(1, 2))
# if we had just added --> return ... it would return ...


# return a type Function


def return_type_function(a):
    return f"so the sum is: {a*a}"


sum = return_type_function(5)
print(sum)
file = open("content.text", "w")
file.write(sum)


def increment(num, by):
    return num + by


print(increment(2, 1))
print(increment(2, by=1))  # still allowed


# likewise here

def multi(num, by=2):
    return num * by


print(multi(3))

# def multi(num, by=2, hello):      #no bro
# def multi(num, hello, by=2):      #yes bro


def show(*num):
    return num


print(show(2, 3, 3))

print('break')


def loop(*num):
    for x in num:
        print(x)
    return x


print(loop(2, 3, 3))


def multiply(*number):
    total = 1
    for x in number:
        total *= x
    return total


print(multiply(1, 2, 3))
