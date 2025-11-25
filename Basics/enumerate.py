# enumerate() is built in python's way to loop thru a sequence while keeping track for both the index and values at the same time

nums = [10, 20, 30, 40]
for i, val in enumerate(nums):
    print(i, val)

# custom start naming index

for i, val in enumerate(nums, start=1):
    print(i, val)

# if we tried using range
for i in range(len(nums)):
    print(i, nums[i])
