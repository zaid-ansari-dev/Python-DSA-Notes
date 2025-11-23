w = "I am a Python Developer"
word = w.split()
print(word)

worde = "hello,hi,bye"
wordi = worde.split()
wording = worde.split(",")
print(wordi)
print(wording)
dash = worde.split("-")
print(dash)  # won't work as it splits on , or - when given in sentences

# u need to
parts = w.split()
hyphenated = "-".join(parts)
print(hyphenated)


# replace method
dashing = worde.replace(",", "-")
print(dashing)


# join:
sentence = ['i', 'am']
sentences = " ".join(sentence)
print(sentences)

fruits = ['apple', 'kiwi']
names = "-".join(fruits)
print(names)
