def grade(current_grade):

    if 2 <= current_grade <= 2.99:
        print("Fail")
    elif current_grade <= 3.49:
        print("Poor")
    elif current_grade <= 4.49:
        print("Good")
    elif current_grade <= 5.49:
        print("Very Good")
    elif current_grade <= 6:
        print("Excellent")

grade(float(input()))

