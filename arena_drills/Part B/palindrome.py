# 9. The Palindrome Check(Manual)
# •	Task: Check if a string is the same forwards and backwards. Use left and right variables.
# •	Input: "racecar" -> Output: True
# •	Input: "hello" -> Output: False
def palindrome(string):
    og = string
    reverse = list(string)
    start = 0
    end = len(reverse) - 1
    while start < end:
        reverse[start], reverse[end] = reverse[end], reverse[start]
        start += 1
        end -= 1
    print(reverse)  # just checking
    reverse = "".join(reverse)
    if og == reverse:
        return True
    else:
        return False


print(palindrome("racecar"))
print(palindrome("hello"))
