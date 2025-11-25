tup = (1, 2, 3, 1)
print(tup)
t = (1)
print(type(t))

# to make an empty tupe
tongs = (1,)
print(type(tongs))

# immutable
# order indexing exists

nums = (1, 2, 3, 4, 5, 6, 7)
print(nums[3])
print(nums[4])
print(nums[-1])

if 3 in nums:
    print('yes')

tup2 = tup[1:-1]
print(tup2)
