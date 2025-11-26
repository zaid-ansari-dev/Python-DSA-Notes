# 1672 : Richest Customer Wealth

def wealth(money):
    arr = []
    for i in money:
        count = 0
        for j in i:
            count += j
        arr.append(count)
    maxi = arr[0]
    for i in range(1, len(arr)):
        if maxi < arr[i]:
            maxi = arr[i]
    return maxi


print(wealth([[1, 2, 3], [3, 2, 1]]))
print(wealth([[1, 5], [7, 3], [3, 5]]))
print(wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
