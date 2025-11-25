# zip is used to pair up elements from multiple iterables

nums = [1, 2, 3]
lames = ['a', 'b', 'c']
for n, l in zip(nums, lames):
    print(n, l)

symbols = ["!", "#", "$"]
print(list(zip(nums, lames, symbols)))

# zip stops at shortest iterables
short = ['u', 'v']
print(list(zip(nums, short)))
