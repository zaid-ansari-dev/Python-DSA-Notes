seen = set()

seen.add(5)

if 5 in seen:
    print("found")

nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))  # to remove duplicates
print(unique)

# if you want to remove duplicates while preserving order use
unique_ordered = list(dict.fromkeys(nums))
print(unique_ordered)

uniques = []
for n in nums:
    if n not in seen:
        seen.add(n)
        uniques.append(n)

print(seen)
print("seen")
print(uniques)

numbers = {3, 3, 3}
dupli = set(numbers)
print(dupli)

# append used in lists and add used in sets
