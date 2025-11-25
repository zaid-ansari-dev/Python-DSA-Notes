count = 0
for x in range(1, 11):
    if x % 2 == 0:
        count += 1
        print(x)
print("Count of even no: ", count)
print(f"We got count: {count} numbers")

for x in range(2, 9, 2):
    print(x)
