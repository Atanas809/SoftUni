# Person type:
age = float(input())
gender = input()

type_of_person = ""

if gender == "m" and age >= 16:
    type_of_person = "Mr."
elif gender == "m" and age < 16:
    type_of_person = "Master"
elif gender == "f" and age >= 16:
    type_of_person = "Ms."
else:
    type_of_person = "Miss"

print(type_of_person)
