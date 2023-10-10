from unittest import TestCase, main

from structure_and_functionality_4.movie import Movie


class MovieTests(TestCase):
    def test_init_is_initialized_correctly(self):
        movie = Movie("Max", 1999, 10)

        self.assertEqual("Max", movie.name)
        self.assertEqual(1999, movie.year)
        self.assertEqual(10, movie.rating)
        self.assertEqual([], movie.actors)

    def test_name_with_empty_value_raises(self):
        movie = Movie("Max", 1999, 10)

        with self.assertRaises(ValueError) as ex:
            movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_year_with_invalid_year_below_1887_raises(self):
        movie = Movie("Max", 1999, 10)

        with self.assertRaises(ValueError) as ex:
            movie.year = 1700

        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_non_existing_actor_appends_correctly(self):
        movie = Movie("Max", 1999, 10)

        self.assertEqual([], movie.actors)

        movie.add_actor("Ivan")

        self.assertEqual(["Ivan"], movie.actors)

    def test_add_existing_actor_returning_correct_message(self):
        movie = Movie("Max", 1999, 10)

        self.assertEqual([], movie.actors)

        movie.add_actor("Ivan")

        self.assertEqual(["Ivan"], movie.actors)

        result = movie.add_actor("Ivan")
        expected_result = "Ivan is already added in the list of actors!"

        self.assertEqual(expected_result, result)
        self.assertEqual(["Ivan"], movie.actors)

    def test_self_gt_other_returns_correct_message(self):
        movie = Movie("Max", 1999, 11)
        movie1 = Movie("Vayne", 1999, 10)

        result = movie > movie1
        expected_result = '"Max" is better than "Vayne"'

        self.assertEqual(expected_result, result)

    def test_other_gt_self_returns_correct_message(self):
        movie = Movie("Max", 1999, 10)
        movie1 = Movie("Vayne", 1999, 11)

        result = movie > movie1
        expected_result = '"Vayne" is better than "Max"'

        self.assertEqual(expected_result, result)

    def test_repr_method_returning_correct_message(self):
        movie = Movie("Max", 1999, 10)
        self.assertEqual([], movie.actors)

        movie.add_actor("Ivan")

        self.assertEqual(["Ivan"], movie.actors)

        result = repr(movie)
        expected_result = 'Name: Max\nYear of Release: 1999\nRating: 10.00\nCast: Ivan'

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
