temp = 34
if temp > 45:
    print("it's warm")
    print("drink water")
elif temp < 45:
    print("it's nice")
    print("say hello to the world")
print("Done")


# exercise real world

age = 21
if age > 18:
    message = "Eligible"
else:
    message = "not-eligible"
print(message)

# easier with TERNEARY OPS
time = 8
decide = "play" if time < 7 else "don't play"
print(decide)


# ops and,or,not

high_income = True
low_income = True
student = False

if high_income and low_income:
    print("eligible")
elif student and low_income:
    print("not-allowed")
elif student or low_income:  # stopped bcuz previous condition above matched so cycle breaks
    print("allowed")
elif not low_income:
    print("no way")
else:
    print("not eligible")


# short-circuit evaluation
if high_income or low_income or not student:
    print('go on')

# a good print
# if high_income and good_credit_score and not student:
#   print("Eligible")

if age >= 18 and age <= 65:
    print("congrats")
if 18 <= age <= 65:
    print("still congo")

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
