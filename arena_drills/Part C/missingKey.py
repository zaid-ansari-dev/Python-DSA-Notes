# 17. The "Missing" Key
# •	Task: You have a list of expected keys ["id", "name", "email"]. Check if the dictionary {"id": 1, "name": "Gemini"} is missing any of them. Print the missing key.
# •	Output: "email"

std = ["id", "name", "email"]


def find(user):
    for key in std:
        if key not in user:
            return f"{key} missing"


print(find({"id": 1, "name": "Gemini"}))
