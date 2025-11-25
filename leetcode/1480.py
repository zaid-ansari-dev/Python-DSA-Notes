# 1480 : Running Sum of 1d Array

def run(nums):
    for i in range(len(nums)):
        if i == 0:
            nums[i] = nums[i]
        else:
            nums[i] = nums[i-1] + nums[i]
    return nums


print(run([1, 2, 3, 4]))
print(run([1, 1, 1, 1]))


def RUN(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums


print(RUN([1, 2, 3, 4]))
print(RUN([1, 1, 1, 1]))
