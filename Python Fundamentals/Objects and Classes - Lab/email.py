# Задача 3:

class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):

        self.is_sent = True

    def __repr__(self):

        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

info = input().split()

mails = list()

while info[0] != "Stop":

    sender = info[0]
    receiver = info[1]
    content = info[2]

    email = Email(sender, receiver, content)

    mails.append(email)

    info = input().split()

indices = list(map(int, input().split(", ")))

for x in indices:
    mails[x].send()

for y in mails:
    print(y)

