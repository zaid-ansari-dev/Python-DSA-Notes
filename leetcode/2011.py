# 2011 : Final Value of Variable After Performing Operations

def var(lists):
    x = 0
    for i in lists:
        if "++" in i:
            x = x + 1
        else:
            x = x - 1
    return x


print(var(["--x", "x++", "x++"]))
print(var(["++X", "++X", "X++"]))
print(var(["X++", "++X", "--X", "X--"]))
