def bmi_calculator():

    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))

    height = height / 100
    BMI = weight / (height * height)

    print(f"Your Body Mass Index is: {BMI:.2f}")

    if BMI > 0:

        if BMI <= 16:
            print("You are severely underweight")

        elif BMI <= 18.5:
            print("You are underweight")

        elif BMI <= 25:
            print("You are Healthy")

        elif BMI <= 30:
            print("You are overweight")

        else:
            print("You are severely overweight")

    else:
        print("Please enter valid details!")
        bmi_calculator()

bmi_calculator()
