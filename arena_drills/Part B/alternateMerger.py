# 11. The Alternate Merger
# •	Task: Combine two lists of equal length by taking one item from A, then one from B, then A...
# •	Input: A=[1, 2], B=[3, 4]
# •	Output: [1, 3, 2, 4]

def merger(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
    return result


print(merger([1, 2], [3, 4]))
