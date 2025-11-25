# 15. The Grade Lookup
# •	Task: Given a dictionary {"Alice": 85, "Bob": 90}, print "Bob passed" if his score is > 50, else print "Bob failed".
# •	Output: "Bob passed"

dicti = {"Alice": 49, "Bob": 90}

# first
if dicti["Bob"] > 50:
    print("Bob passed")
else:
    print("Bob failed")

# second
for key, value in dicti.items():
    if key == "Bob":
        if value > 50:
            print(f"{key} passed")
        else:
            print(f"{key} failed")


# general
for key, value in dicti.items():
    if value < 50:
        print(f"{key} failed")
    else:
        print(f"{key} passed")
