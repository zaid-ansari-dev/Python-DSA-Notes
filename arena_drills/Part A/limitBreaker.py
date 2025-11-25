# 6. The Limit Breaker
# •	Task: Return True if all numbers in the list are greater than 10. Otherwise return False.
# •	Input: [11, 20, 15] -> Output: True
# •	Input: [11, 5, 20] -> Output: False

def breaker(lists):
    for num in lists:
        if num < 10:
            return False
    return True


print(breaker([11, 20, 15]))
print(breaker([11, 5, 20]))


# there exists a method as well

# return all(num > 10 for num in lists) # return true or false
