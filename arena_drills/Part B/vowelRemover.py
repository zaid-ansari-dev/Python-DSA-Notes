# 10. The "Vowel" Remover
# •	Task: Create a new string with all vowels (a, e, i, o, u) removed.
# •	Input: "openai"
# •	Output: "pn"
#

# s = ""
# st = str()
# print(len(s))
# print(len(st))
# print(st == "")

def remover(text):
    vowels = "aeiou"
    result = ""
    for ch in text:
        if ch not in vowels:
            result += ch
    return result


print(remover("openai"))

# list comprehension
# def remover(text):
#     vowels = "aeiou"
#     return "".join([ch for ch in text if ch not in vowels])
