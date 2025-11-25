# 18. The Value Sum
# •	Task: Calculate the sum of all values in a dictionary.
# •	Input: {"a": 10, "b": 20}
# •	Output: 30

dic = {"a": 10, "b": 20}
count = 0
for value in dic.values():
    count += value

print(count)

# more direct
print(sum(dic.values()))
