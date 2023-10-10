from unittest import TestCase, main

from structure_and_functionality.library import Library


class LibraryTests(TestCase):
    def test_init_is_initialized_correctly(self):
        library = Library("Nevena")

        self.assertEqual("Nevena", library.name)
        self.assertEqual({}, library.books_by_authors)
        self.assertEqual({}, library.readers)

    def test_name_setter_if_empty_raises(self):
        library = Library("Nevena")

        with self.assertRaises(ValueError) as ex:
            library.name = ""

        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book_if_author_and_title_not_in_books_by_authors_create_it(self):
        library = Library("Nevena")

        self.assertEqual({}, library.books_by_authors)

        library.add_book("Johnny", "Harry Potter")

        self.assertEqual({"Johnny": ["Harry Potter"]}, library.books_by_authors)

    def test_add_book_if_only_the_title_not_in_authors_books_dict(self):
        library = Library("Nevena")

        self.assertEqual({}, library.books_by_authors)

        library.add_book("Johnny", "Harry Potter")

        self.assertEqual({"Johnny": ["Harry Potter"]}, library.books_by_authors)

        library.add_book("Johnny", "Winks")

        self.assertEqual({"Johnny": ["Harry Potter", "Winks"]}, library.books_by_authors)

    def test_add_book_if_title_exists_pass(self):
        library = Library("Nevena")

        self.assertEqual({}, library.books_by_authors)

        library.add_book("Johnny", "Harry Potter")

        self.assertEqual({"Johnny": ["Harry Potter"]}, library.books_by_authors)

        library.add_book("Johnny", "Harry Potter")

        self.assertEqual({"Johnny": ["Harry Potter"]}, library.books_by_authors)

    def test_add_non_existing_reader_then_chek_if_we_add_him_correctly(self):
        library = Library("Nevena")
        self.assertEqual({}, library.readers)

        library.add_reader("Ivan")
        self.assertEqual({"Ivan": []}, library.readers)
        library.add_reader("Gogo")
        self.assertEqual({"Ivan": [], "Gogo": []}, library.readers)

    def test_add_existing_reader_returns_correct_message(self):
        library = Library("Nevena")
        self.assertEqual({}, library.readers)

        library.add_reader("Ivan")
        self.assertEqual({"Ivan": []}, library.readers)
        result = library.add_reader("Ivan")
        expected_result = "Ivan is already registered in the Nevena library."
        self.assertEqual(expected_result, result)
        self.assertEqual({"Ivan": []}, library.readers)

    def test_rent_book_with_invalid_reader_name_returns_correct_message(self):
        library = Library("Nevena")
        self.assertEqual({}, library.readers)

        result = library.rent_book("Ivan", "Tonny", "Harry Potter")
        expected_result = "Ivan is not registered in the Nevena Library."
        self.assertEqual(expected_result, result)

    def test_rent_book_if_book_author_non_existing_returns_correct_message(self):
        library = Library("Nevena")

        self.assertEqual({}, library.books_by_authors)
        self.assertEqual({}, library.readers)

        library.add_reader("Ivan")
        self.assertEqual({"Ivan": []}, library.readers)

        library.add_book("Johnny", "Harry Potter")
        self.assertEqual({"Johnny": ["Harry Potter"]}, library.books_by_authors)

        result = library.rent_book("Ivan", "Tonny", "Harry Potter")
        expected_result = "Nevena Library does not have any Tonny's books."
        self.assertEqual(expected_result, result)

    def test_rent_book_if_book_title_non_existing_returns_correct_message(self):
        library = Library("Nevena")

        self.assertEqual({}, library.books_by_authors)
        self.assertEqual({}, library.readers)

        library.add_reader("Ivan")
        self.assertEqual({"Ivan": []}, library.readers)

        library.add_book("Johnny", "Harry Potter")
        self.assertEqual({"Johnny": ["Harry Potter"]}, library.books_by_authors)

        result = library.rent_book("Ivan", "Johnny", "Don Omar")
        expected_result = """Nevena Library does not have Johnny's "Don Omar"."""
        self.assertEqual(expected_result, result)

    def test_rent_book_added_correctly_to_reader_name_dict(self):
        library = Library("Nevena")

        self.assertEqual({}, library.books_by_authors)
        self.assertEqual({}, library.readers)

        library.add_reader("Ivan")
        self.assertEqual({"Ivan": []}, library.readers)

        library.add_book("Johnny", "Harry Potter")
        self.assertEqual({"Johnny": ["Harry Potter"]}, library.books_by_authors)
        library.add_book("Johnny", "Don Omar")
        self.assertEqual({"Johnny": ["Harry Potter", "Don Omar"]}, library.books_by_authors)

        library.rent_book("Ivan", "Johnny", "Harry Potter")

        self.assertEqual({"Ivan": [{"Johnny": "Harry Potter"}]}, library.readers)
        self.assertEqual({"Johnny": ["Don Omar"]}, library.books_by_authors)


if __name__ == "__main__":
    main()
