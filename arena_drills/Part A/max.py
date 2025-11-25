# 2. The "Max" Hunter
# •	Task: Find the largest number in a list without using max(). Assume the list is not empty.
# •	Input: [5, 12, 3, 8]
# •	Output: 12

lists = [5, 12, 3, 8]
# naive::
# largest = lists[0]
# for i in lists:
#     if largest < i:
#         largest = i

# print(largest)


# refined:

def find_largest(nums):
    largest = nums[0]
    for num in nums[1:]:
        if largest < num:
            largest = num

    return largest


print(find_largest([5, 3, 6, 2]))
