# 8. The Manual Reverse
# •	Task: Create a new list that is the reverse of the input list. Loop backwards.
# •	Input: [1, 2, 3]
# •	Output: [3, 2, 1]

lists = [1, 2, 3]
start = 0
end = len(lists) - 1
while start < end:
    lists[start], lists[end] = lists[end], lists[start]
    start += 1
    end -= 1

print(lists)


# python helped
# for num in lists[::-1]:
#     print(num)


# Initial: [1, 2, 3, 4]
# Pointers:  ^           ^
#            start=0     end=3

# Step 1: swap → [4, 2, 3, 1]
# Pointers:     ^     ^
#               start=1 end=2

# Step 2: swap → [4, 3, 2, 1]
# Pointers:       ^ ^
#                 start=2 end=1 → condition fails → stop
