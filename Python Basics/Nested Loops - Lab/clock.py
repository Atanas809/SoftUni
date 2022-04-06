 for hour in range(0, 24):
    for minutes in range(0, 60):
        print(f"{hour}:{minutes}")
        if minutes < 10:
            print(f"{hour}:0{minutes}")
        else:
            print(f"{hour}:{minutes}")
