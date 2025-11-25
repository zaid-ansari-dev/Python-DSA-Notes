# 1929 : Concatenation of Array

def concat(nums):
    ans = []
    n = len(nums)
    for i in range(len(nums)*2):
        ans.append(nums[i % n])
    return ans


print(concat([1, 2, 1]))
print(concat([1, 3, 2, 1]))
