print(type(range(2)))

for x in "Python":
    print(x)
print('\n')
for x in [1, 2, 3]:
    print(x)

cart = ["toy", "boy"]
for item in cart:
    print(item)


number = 100
while number > 0:
    print(number)
    number //= 2


# nice one bro cmd copying
# AMATEURS
command = ""
while command != "quit" and command != "QUIT":
    command = input(">")
    print("ECHO", command)

# for PROs
cmd = ""
while cmd.lower() != "quit":
    cmd = input(">")
    print("ECHO", cmd)

# also for PROs
input = ""
while True:            # Infinite loop
    input = input(">")
    print("ECHO", input)
    if input.lower() == "quit":
        break
