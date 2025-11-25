# 4. The Even Filter
# •	Task: Create a new list that contains only the even numbers from the input list.
# •	Input: [1, 2, 3, 4, 5, 6]
# •	Output: [2, 4, 6]

lists = [1, 2, 3, 4, 5, 6]
for num in lists:
    if num % 2 == 0:
        print(num)
