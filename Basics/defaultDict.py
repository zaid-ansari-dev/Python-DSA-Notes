from collections import defaultdict

my_dict = defaultdict(int)

print(my_dict)

print(my_dict["age"])
my_dict["year"] += 1
print(my_dict)


myChar = ["a", "c", "a", "b", "d", "e", "e"]
counter = defaultdict(int)
for i in myChar:
    counter[i] += 1

print(counter)

words = ["apple", "banana", "brocoli", "avacado", "orange", "carrot"]
grouped_words = defaultdict(list)

for word in words:
    grouped_words[word[0]].append(word)

print(grouped_words)
