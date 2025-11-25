# 3. The "Specific" Counter
# •	Task: Count how many times the number 7 appears in a list.
# •	Input: [1, 7, 2, 7, 7, 3]
# •	Output: 3


from collections import Counter
from collections import defaultdict
lists = [1, 7, 2, 7, 7, 3]
count = 0
for num in lists:
    if num == 7:
        count += 1

print(f"count of 7 is: {count}")


# if you trynna count each frequency then...

freq = {}
for num in lists:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)


# cleaner with defaultdict


frequency = defaultdict(int)

for num in lists:
    frequency[num] += 1

print('break')
print(dict(frequency))
print(frequency)


# way easier with Counter

occur = Counter(lists)
print('break2')
print(occur)
