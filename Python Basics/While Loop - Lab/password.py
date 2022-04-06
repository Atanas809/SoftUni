username = input()
password = input()

entered_password = input()

while entered_password != password:
    entered_password = input()
print(f"Welcome {username}!")
