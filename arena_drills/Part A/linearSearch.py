# 7. The Index Finder (Linear Search)
# •	Task: Return the index of the number 99. If it's not there, return -1.
# •	Input: [10, 20, 99, 30]
# •	Output: 2

def search(lists):
    for num in range(len(lists)):
        if lists[num] == 99:
            return num
    return -1


print(search([10, 20, 99, 30]))
