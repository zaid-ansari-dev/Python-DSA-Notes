# 1920 : Build Array from Permutation

# ans[i] = nums[nums[i]]
def build(nums):
    ans = []
    for i in range(len(nums)):
        ans.append(nums[nums[i]])

    return ans


print(build([0, 2, 1, 4, 5, 3]))
print(build([5, 0, 1, 2, 3, 4]))
