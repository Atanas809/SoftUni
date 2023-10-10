from structure_and_functionality_2.movie_specification.movie import Movie


class Fantasy(Movie):
    MIN_AGE_RESTRICTION = 6

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = MIN_AGE_RESTRICTION):
        super().__init__(title, year, owner, age_restriction)

    def movie_type(self):
        return "Fantasy"

    def details(self):
        return f"Fantasy - " \
               f"Title:{self.title}, " \
               f"Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, " \
               f"Owned by:{self.owner.username}"
