# 1470 : Shuffle the Array

def shuffle(arr):
    length = len(arr)
    middle = int(length / 2)
    new = []
    for i in range(middle):
        new.append(arr[i])
        new.append(arr[i+middle])
    return new


print(shuffle([2, 5, 1, 3, 4, 7]))
