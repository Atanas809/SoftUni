hour_exam = int(input())
minutes_exam = int(input())
hour_arriving = int(input())
minutes_arriving = int(input())

exam_in_minutes = hour_exam * 60 + minutes_exam
arriving_in_minutes = hour_arriving * 60 + minutes_arriving

if arriving_in_minutes > exam_in_minutes:
    print("Late")

elif exam_in_minutes - 30 <= arriving_in_minutes <= exam_in_minutes:
    print("On time")

elif exam_in_minutes - 30 > arriving_in_minutes:
    print("Early")

if exam_in_minutes - 60 < arriving_in_minutes < exam_in_minutes:
    minutes_before_exam = abs(exam_in_minutes - arriving_in_minutes)
    print(f"{minutes_before_exam} minutes before the start")

elif exam_in_minutes - 60 >= arriving_in_minutes:
    difference = abs(exam_in_minutes - arriving_in_minutes)
    hours = difference // 60
    minutes = difference % 60
    if minutes < 10:
        print(f"{hours}:0{minutes} hours before the start")
    else:
        print(f"{hours}:{minutes} hours before the start")
elif exam_in_minutes < arriving_in_minutes < exam_in_minutes + 60:
    minutes_after = abs(arriving_in_minutes - exam_in_minutes)
    print(f"{minutes_after} minutes after the start")
elif exam_in_minutes + 60 <= arriving_in_minutes:
    difference = abs(exam_in_minutes - arriving_in_minutes)
    hours = difference // 60
    minutes = difference % 60
    if minutes < 10:
        print(f"{hours}:0{minutes} hours after the start")
    else:
        print(f"{hours}:{minutes} hours after the start")
