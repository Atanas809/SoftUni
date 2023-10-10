from unittest import TestCase, main

from projects.list import IntegerList


class IntegerListTests(TestCase):
    def test_init_with_integer_values(self):
        my_list = IntegerList(1, 2, 3)

        self.assertEqual([1, 2, 3], my_list.get_data())

    def test_init_with_invalid_types(self):
        my_list = IntegerList(1, "2", 3)

        self.assertEqual([1, 3], my_list.get_data())

    def test_add_if_not_integer_raises(self):
        my_list = IntegerList(1, 2, 3)

        with self.assertRaises(ValueError) as ex:
            my_list.add("4")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_with_valid_value(self):
        my_list = IntegerList(1, 2, 3)

        result = my_list.add(4)

        self.assertEqual([1, 2, 3, 4], result)

    def test_remove_invalid_index_raises(self):
        my_list = IntegerList(1, 2, 3)

        with self.assertRaises(IndexError) as ex:
            my_list.remove_index(3)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_valid_index(self):
        my_list = IntegerList(1, 2, 3)

        result = my_list.remove_index(2)

        self.assertEqual(3, result)
        self.assertEqual([1, 2], my_list.get_data())

    def test_get_element_with_invalid_index_raises(self):
        my_list = IntegerList(1, 2, 3)

        with self.assertRaises(IndexError) as ex:
            my_list.get(3)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_element_with_valid_index(self):
        my_list = IntegerList(1, 2, 3)

        result = my_list.get(1)

        self.assertEqual(2, result)
        self.assertEqual([1, 2, 3], my_list.get_data())

    def test_insert_value_on_invalid_index_raises(self):
        my_list = IntegerList(1, 2, 3)

        with self.assertRaises(IndexError) as ex:
            my_list.insert(3, 4)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_value_with_invalid_type_raises(self):
        my_list = IntegerList(1, 2, 3)

        with self.assertRaises(ValueError) as ex:
            my_list.insert(1, "4")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_value_with_correct_parameters(self):
        my_list = IntegerList(1, 2, 3)

        my_list.insert(0, 4)

        self.assertEqual([4, 1, 2, 3], my_list.get_data())

    def test_get_biggest_element(self):
        my_list = IntegerList(1, 2, 7, 99, 100, 3)

        result = my_list.get_biggest()

        self.assertEqual(100, result)

    def test_get_index_by_element(self):
        my_list = IntegerList(1, 2, 3)

        result = my_list.get_index(1)

        self.assertEqual(0, result)


if __name__ == "__main__":
    main()
