# 20. The "Two List" Zipper
# •	Task: You have two lists: names = ["Alice", "Bob"] and scores = [85, 90]. Create a dictionary {"Alice": 85, "Bob": 90} using a loop.

names = ["Alice", "Bob"]
scores = [85, 90]
newDic = {}
length = len(names)
for i in range(length):
    newDic[names[i]] = scores[i]

print(newDic)

# by trick
dicti = dict(zip(names, scores))
print(dicti)
