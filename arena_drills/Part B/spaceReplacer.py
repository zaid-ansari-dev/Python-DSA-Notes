# 12. The Space Replacer
# •	Task: Replace every space " " in a string with a dash "-". (Don't use .replace()).
# •	Input: "hello world"
# •	Output: "hello-world"

string = "hello world"
result = []
for i in string:
    if i == " ":
        result.append("-")
    if i != " ":
        result.append(i)
result = "".join(result)
print(result)


# lil better

def one(string):
    result = ""
    for i in string:
        if i == " ":
            result += "-"
        else:
            result += i
    result = "".join(result)
    return result


print(one("hello world"))
