class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        name = f"{self.name} {other.name}"
        all_people = self.people + other.people

        return Group(name, all_people)

    def __str__(self):
        members = ', '.join(str(name) for name in self.people)
        return f"Group {self.name} with members {members}"

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index]}"
