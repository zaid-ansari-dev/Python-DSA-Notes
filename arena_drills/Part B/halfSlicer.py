# 13. The "First Half" Slicer
# •	Task: Print the first half of a list. If the length is odd, include the middle element.
# •	Input: [1, 2, 3, 4, 5]
# •	Output: [1, 2, 3]

def slicer(lists):
    length = len(lists)
    middle = length // 2
    if length % 2 != 0:
        middle += 1
        return lists[:middle]
    else:
        return lists


print(slicer([1, 2, 3, 4, 5]))
print(slicer([10, 20, 30, 40, 50]))
