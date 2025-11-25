# 19. The Filtered Map
# •	Task: Create a new dictionary containing only items where the value is greater than 100.
# •	Input: {"a": 50, "b": 150, "c": 200}
# •	Output: {"b": 150, "c": 200}

dic = {"a": 50, "b": 150, "c": 200}
newDic = {}
for key, value in dic.items():
    if value > 100:
        newDic[key] = value

print(newDic)
