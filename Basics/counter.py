from collections import Counter

c = Counter("banana")
print(c)

nums = [1, 2, 3, 4, 5]
d = Counter(nums)
print(d)

print(c.most_common(2))
print(d.most_common(2))
