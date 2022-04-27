class Party:

    def __init__(self):
        self.people = list()

    def going(self, name):

        while name != "End":

            self.people.append(name)

            name = input()

        return self.people

party = Party()

names = input()

people_going = party.going(names)

print(f"Going: {', '.join(people_going)}")
print(f"Total: {len(people_going)}")


