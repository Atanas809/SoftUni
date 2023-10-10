from unittest import TestCase, main

from project.bookstore import Bookstore


class BookstoreTests(TestCase):
    def test_init_is_initialized_correctly(self):
        store = Bookstore(5)

        self.assertEqual(5, store.books_limit)
        self.assertEqual({}, store.availability_in_store_by_book_titles)
        self.assertEqual(0, store.total_sold_books)

    def test_book_limit_with_zero_value_raises(self):
        store = Bookstore(5)

        with self.assertRaises(ValueError) as ex:
            store.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ex.exception))

    def test_dict_keys_is_strings(self):
        store = Bookstore(5)

        self.assertEqual({}, store.availability_in_store_by_book_titles)

        store.receive_book("Mad Max", 2)
        self.assertEqual({"Mad Max": 2}, store.availability_in_store_by_book_titles)

        self.assertSetEqual(set(map(type, store.availability_in_store_by_book_titles.keys())), {str})

    def test_dict_values_is_integers(self):
        store = Bookstore(5)

        self.assertEqual({}, store.availability_in_store_by_book_titles)

        store.receive_book("Mad Max", 2)
        self.assertEqual({"Mad Max": 2}, store.availability_in_store_by_book_titles)

        self.assertSetEqual(set(map(type, store.availability_in_store_by_book_titles.values())), {int})

    def test_book_limit_with_negative_value_raises(self):
        store = Bookstore(5)

        with self.assertRaises(ValueError) as ex:
            store.books_limit = -1

        self.assertEqual("Books limit of -1 is not valid", str(ex.exception))

    def test_len_method_returns_correct_value_without_adding_values_to_dict(self):
        store = Bookstore(5)

        result = len(store)

        self.assertEqual(0, result)

    def test_len_method_returns_correct_value_when_added_values_to_dict(self):
        store = Bookstore(5)
        book = "Mad Max"
        num_books = 2

        self.assertIsInstance(book, str)
        self.assertIsInstance(num_books, int)

        self.assertEqual({}, store.availability_in_store_by_book_titles)

        store.receive_book(book, num_books)
        self.assertEqual({book: num_books}, store.availability_in_store_by_book_titles)

        result = len(store)

        self.assertEqual(2, result)

        store.receive_book(book, num_books)
        self.assertEqual({book: num_books + 2}, store.availability_in_store_by_book_titles)

        result1 = len(store)

        self.assertEqual(4, result1)

        self.assertSetEqual(set(map(type, store.availability_in_store_by_book_titles.keys())), {str})
        self.assertSetEqual(set(map(type, store.availability_in_store_by_book_titles.values())), {int})

    def test_receive_book_with_non_existing_book_title(self):
        store = Bookstore(5)
        book = "Mad Max"
        num_books = 2

        self.assertIsInstance(book, str)
        self.assertIsInstance(num_books, int)

        self.assertEqual({}, store.availability_in_store_by_book_titles)

        result = store.receive_book(book, num_books)
        expected_result = "2 copies of Mad Max are available in the bookstore."

        self.assertEqual(expected_result, result)
        self.assertEqual({"Mad Max": 2}, store.availability_in_store_by_book_titles)
        self.assertSetEqual(set(map(type, store.availability_in_store_by_book_titles.keys())), {str})
        self.assertSetEqual(set(map(type, store.availability_in_store_by_book_titles.values())), {int})

    def test_receive_book_with_existing_book_title(self):
        store = Bookstore(5)
        book = "Mad Max"
        num_books = 2

        self.assertIsInstance(book, str)
        self.assertIsInstance(num_books, int)

        self.assertEqual({}, store.availability_in_store_by_book_titles)
        store.receive_book(book, num_books)
        self.assertEqual({"Mad Max": 2}, store.availability_in_store_by_book_titles)

        result = store.receive_book(book, num_books)
        expected_result = "4 copies of Mad Max are available in the bookstore."

        self.assertEqual(expected_result, result)
        self.assertEqual({"Mad Max": 4}, store.availability_in_store_by_book_titles)
        self.assertSetEqual(set(map(type, store.availability_in_store_by_book_titles.keys())), {str})
        self.assertSetEqual(set(map(type, store.availability_in_store_by_book_titles.values())), {int})

    def test_receive_book_when_books_limit_less_then_books_to_add_raises(self):
        store = Bookstore(2)
        book = "Mad Max"
        num_books = 2

        self.assertIsInstance(book, str)
        self.assertIsInstance(num_books, int)

        self.assertEqual({}, store.availability_in_store_by_book_titles)
        store.receive_book(book, num_books)
        self.assertEqual({"Mad Max": 2}, store.availability_in_store_by_book_titles)

        with self.assertRaises(Exception) as ex:
            store.receive_book(book, num_books)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))
        self.assertSetEqual(set(map(type, store.availability_in_store_by_book_titles.keys())), {str})
        self.assertSetEqual(set(map(type, store.availability_in_store_by_book_titles.values())), {int})

    def test_sell_book_with_possible_amount_to_sell(self):
        store = Bookstore(5)
        book = "Mad Max"
        num_books = 2

        self.assertIsInstance(book, str)
        self.assertIsInstance(num_books, int)

        self.assertEqual({}, store.availability_in_store_by_book_titles)
        store.receive_book(book, num_books)
        self.assertEqual({"Mad Max": 2}, store.availability_in_store_by_book_titles)

        result = store.sell_book(book, num_books - 1)
        expected_result = "Sold 1 copies of Mad Max"

        self.assertEqual(expected_result, result)
        self.assertEqual({"Mad Max": 1}, store.availability_in_store_by_book_titles)
        self.assertEqual(1, store.total_sold_books)
        self.assertSetEqual(set(map(type, store.availability_in_store_by_book_titles.keys())), {str})
        self.assertSetEqual(set(map(type, store.availability_in_store_by_book_titles.values())), {int})

    def test_sell_book_with_invalid_book_title_raises(self):
        store = Bookstore(5)
        book = "Mad Max"
        num_books = 2
        new_book = "Mad"

        self.assertIsInstance(book, str)
        self.assertIsInstance(num_books, int)

        self.assertEqual({}, store.availability_in_store_by_book_titles)
        store.receive_book(book, num_books)
        self.assertEqual({"Mad Max": 2}, store.availability_in_store_by_book_titles)

        with self.assertRaises(Exception) as ex:
            store.sell_book(new_book, num_books)

        self.assertEqual("Book Mad doesn't exist!", str(ex.exception))

    def test_sell_book_with_invalid_number_of_books_raises(self):
        store = Bookstore(5)
        book = "Mad Max"
        num_books = 2

        self.assertIsInstance(book, str)
        self.assertIsInstance(num_books, int)

        self.assertEqual({}, store.availability_in_store_by_book_titles)
        store.receive_book(book, num_books)
        self.assertEqual({"Mad Max": 2}, store.availability_in_store_by_book_titles)

        with self.assertRaises(Exception) as ex:
            store.sell_book(book, num_books + 1)

        self.assertEqual("Mad Max has not enough copies to sell. Left: 2", str(ex.exception))
        self.assertEqual({"Mad Max": 2}, store.availability_in_store_by_book_titles)
        self.assertSetEqual(set(map(type, store.availability_in_store_by_book_titles.keys())), {str})
        self.assertSetEqual(set(map(type, store.availability_in_store_by_book_titles.values())), {int})

    def test_str_method_returning_correct_string_with_non_empty_dict(self):
        store = Bookstore(5)
        book = "Mad Max"
        num_books = 2

        self.assertIsInstance(book, str)
        self.assertIsInstance(num_books, int)

        self.assertEqual({}, store.availability_in_store_by_book_titles)
        store.receive_book(book, num_books)
        self.assertEqual({"Mad Max": 2}, store.availability_in_store_by_book_titles)

        store.sell_book(book, num_books - 1)
        self.assertEqual({"Mad Max": 1}, store.availability_in_store_by_book_titles)

        result = str(store)
        expected_result = """Total sold books: 1
Current availability: 1
 - Mad Max: 1 copies"""

        self.assertEqual(expected_result, result)
        self.assertSetEqual(set(map(type, store.availability_in_store_by_book_titles.keys())), {str})
        self.assertSetEqual(set(map(type, store.availability_in_store_by_book_titles.values())), {int})

    def test_str_method_returning_correct_string_with_empty_dict(self):
        store = Bookstore(5)

        self.assertEqual({}, store.availability_in_store_by_book_titles)

        result = str(store)
        expected_result = 'Total sold books: 0\nCurrent availability: 0'

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
