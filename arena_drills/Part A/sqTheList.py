# 5. The "Double" Transformation
# •	Task: Update a list so that every number is multiplied by 2 in-place (don't create a new list).
# •	Input: [1, 2, 3]
# •	Output: [2, 4, 6]

lists = [1, 2, 3]

for i in range(len(lists)):
    lists[i] = lists[i] ** 2

print(lists)


lists = [x*x for x in lists]
print(lists)
