from calendar import month_name


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def is_allowed_to_watch(self, age):
        return age >= self.age_restriction

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month, year = date.split(".")
        string_month = month_name[int(month)]
        year = int(year)
        return cls(name, id, year, string_month, age_restriction)

    def __repr__(self):
        rented_not_rented = "rented" if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {rented_not_rented}"
