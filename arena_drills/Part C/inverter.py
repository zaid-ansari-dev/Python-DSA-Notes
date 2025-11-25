# 16. The Inverter
# •	Task: Swap keys and values. Assume all values are unique.
# •	Input: {"a": 1, "b": 2}
# •	Output: {1: "a", 2: "b"}

dicti = {"a": 1, "b": 2}
newDict = {}
for key, value in dicti.items():
    newDict[value] = key

print(newDict)
