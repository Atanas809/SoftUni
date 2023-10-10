import os

from structure_and_functionality_2.movie_specification.movie import Movie
from structure_and_functionality_2.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        existing_user = self.__find_user_by_username(username)

        if existing_user:
            raise Exception("User already exists!")

        user = User(username, age)

        if user not in self.users_collection:
            self.users_collection.append(user)
            return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)

        if not user:
            raise Exception("This user does not exist!")

        if user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.__find_user_by_username(username)

        if user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        movie.title = kwargs.get("title", movie.title)
        movie.year = kwargs.get("year", movie.year)
        movie.age_restriction = kwargs.get("age_restriction", movie.age_restriction)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)

        if user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)

        if user == movie.owner:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        if user == movie.owner:
            return

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        sorted_movies_by_year_desc = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        result = []

        for movie in sorted_movies_by_year_desc:
            result.append(movie.details())

        return os.linesep.join(x for x in result)

    def __str__(self):
        result = ""
        if self.users_collection:
            result += f"All users: {', '.join([user.username for user in self.users_collection])}\n"
        else:
            result += "All users: No users.\n"

        if self.movies_collection:
            result += f"All movies: {', '.join([movie.title for movie in self.movies_collection])}"
        else:
            result += "All movies: No movies."

        return result

    def __find_user_by_username(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user
