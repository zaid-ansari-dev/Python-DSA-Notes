# 1431 : Kids With the Greatest Number of Candies

def candies(arr, extra):
    result = []
    preMax = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > preMax:
            preMax = arr[i]
    for i in range(len(arr)):
        arr[i] += extra
    for i in range(len(arr)):
        if arr[i] < preMax:
            result.append(False)
        else:
            result.append(True)
    return result


print(candies([2, 3, 5, 1, 3], 3))
print(candies([4, 2, 1, 1, 2], 1))
print(candies([12, 1, 12], 10))


# when u don't mutate it reliefs the time
# like

def go(candies, extraCandies):
    preMax = candies[0]
    result = []
    for i in candies:
        if preMax < i:
            preMax = i
    for i in range(len(candies)):
        if (candies[i] + extraCandies) < preMax:
            result.append(False)
        else:
            result.append(True)

    return result


print(go([2, 3, 5, 1, 3], 3))
print(go([4, 2, 1, 1, 2], 1))
print(go([12, 1, 12], 10))
