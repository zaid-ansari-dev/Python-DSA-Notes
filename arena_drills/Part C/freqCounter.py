# 14. The Frequency Counter (The most important drill)
# •	Task: Loop through a list of words and build a dictionary that counts how many times each word appears.
# •	Input: ["apple", "banana", "apple"]
# •	Output: {"apple": 2, "banana": 1}

from collections import Counter
lists = ["apple", "banana", "apple"]
newLists = {}
for fruit in lists:
    if fruit in newLists:
        newLists[fruit] += 1
    else:
        newLists[fruit] = 1

print(newLists)


# def one(lists):
#     freq = {}
#     for i in lists:
#         freq[i] = freq.get(i, 0) + 1

#     return freq


# print(one(["apple", "kiwi", "apple"]))

# mosts easiest
print(Counter(lists))
