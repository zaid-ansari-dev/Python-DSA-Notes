dict = {
    "name": "zaid",
    "class": "3A",
    "major": "B.Tech",
    4: "yes"
}

print(dict)
print(dict["name"])
print(dict[4])

for key, value in dict.items():
    print(f"{key}: {value}")

print(dict.get("name"))
print(dict.get("name1"))  # returns error when key not exists [this is useful]
print(dict.keys())
print(dict.values())

print("\nbreak\n")

for keys in dict.keys():
    print(keys)
    print(dict[keys])

print("\nbreak\n")

for values in dict.values():
    print(values)
    # print(dict[values])   #error

if "name" in dict:
    print("found")
    print(dict["name"])
else:
    print("not found")

value = dict.get("major")
print(value)
