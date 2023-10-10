from unittest import TestCase, main

from structure_and_funtionality_3.plantation import Plantation


class PlantationTests(TestCase):
    def test_init_is_initialized_correctly(self):
        work = Plantation(3)

        self.assertEqual(3, work.size)
        self.assertEqual({}, work.plants)
        self.assertEqual([], work.workers)

    def test_size_with_negative_value_raises(self):
        work = Plantation(3)

        with self.assertRaises(ValueError) as ex:
            work.size = -2

        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hire_non_existing_worker_returns_correct(self):
        work = Plantation(3)

        result = work.hire_worker("Gogo")
        expected_result = "Gogo successfully hired."

        self.assertEqual(expected_result, result)
        self.assertEqual(["Gogo"], work.workers)

    def test_hire_existing_worker_raises(self):
        work = Plantation(3)

        self.assertEqual([], work.workers)
        work.hire_worker("Gogo")

        with self.assertRaises(ValueError) as ex:
            work.hire_worker("Gogo")

        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_len_method_returning_correct_value(self):
        work = Plantation(3)

        self.assertEqual([], work.workers)
        work.hire_worker("Gogo")
        work.hire_worker("Emma")

        self.assertEqual({}, work.plants)
        work.planting("Gogo", "Rose")
        work.planting("Emma", "Rose")
        self.assertEqual({"Gogo": ["Rose"], "Emma": ["Rose"]}, work.plants)

        result = len(work)
        expected_result = 2

        self.assertEqual(expected_result, result)

    def test_planting_with_invalid_worker_raises(self):
        work = Plantation(3)

        self.assertEqual([], work.workers)

        with self.assertRaises(ValueError) as ex:
            work.planting("gogo", "rose")

        self.assertEqual("Worker with name gogo is not hired!", str(ex.exception))

    def test_planting_with_equal_capacity_than_given_size_raises(self):
        work = Plantation(3)

        self.assertEqual([], work.workers)
        work.hire_worker("Gogo")

        self.assertEqual({}, work.plants)
        work.planting("Gogo", "Rose")
        work.planting("Gogo", "Rose")
        work.planting("Gogo", "Rose")

        with self.assertRaises(ValueError) as ex:
            work.planting("Gogo", "Rose")

        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_with_more_capacity_than_given_size_raises(self):
        work = Plantation(3)

        self.assertEqual([], work.workers)
        work.hire_worker("Gogo")
        work.hire_worker("Emma")
        self.assertEqual(["Gogo", "Emma"], work.workers)

        self.assertEqual({}, work.plants)
        work.plants = {"Gogo": ["Rose", "Rose", "Rose"], "Emma": ["Rose"]}
        self.assertEqual({"Gogo": ["Rose", "Rose", "Rose"], "Emma": ["Rose"]}, work.plants)

        with self.assertRaises(ValueError) as ex:
            work.planting("Gogo", "Rose")

        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_valid_worker_in_plants(self):
        work = Plantation(3)

        self.assertEqual([], work.workers)
        work.hire_worker("Gogo")
        self.assertEqual(["Gogo"], work.workers)

        self.assertEqual({}, work.plants)
        work.planting("Gogo", "Rose")
        self.assertEqual({"Gogo": ["Rose"]}, work.plants)

        result = work.planting("Gogo", "Rose")
        expected_result = "Gogo planted Rose."

        self.assertEqual(expected_result, result)
        self.assertEqual({"Gogo": ["Rose", "Rose"]}, work.plants)

    def test_planting_adding_new_worker_in_plants_dict(self):
        work = Plantation(3)

        self.assertEqual([], work.workers)
        work.hire_worker("Gogo")
        self.assertEqual(["Gogo"], work.workers)

        self.assertEqual({}, work.plants)

        result = work.planting("Gogo", "Rose")
        self.assertEqual({"Gogo": ["Rose"]}, work.plants)
        expected_result = "Gogo planted it's first Rose."

        self.assertEqual(expected_result, result)
        self.assertEqual({"Gogo": ["Rose"]}, work.plants)

    def test_str_method_working_correctly(self):
        work = Plantation(3)

        self.assertEqual([], work.workers)
        work.hire_worker("Gogo")
        self.assertEqual(["Gogo"], work.workers)

        self.assertEqual({}, work.plants)
        work.planting("Gogo", "Rose")
        self.assertEqual({"Gogo": ["Rose"]}, work.plants)

        result = str(work)
        expected_result = 'Plantation size: 3\nGogo\nGogo planted: Rose'

        self.assertEqual(expected_result, result)

    def test_repr_method_working_correctly(self):
        work = Plantation(3)

        self.assertEqual([], work.workers)
        work.hire_worker("Gogo")
        work.hire_worker("Emma")
        self.assertEqual(["Gogo", "Emma"], work.workers)

        self.assertEqual({}, work.plants)
        work.planting("Gogo", "Rose")
        self.assertEqual({"Gogo": ["Rose"]}, work.plants)

        result = repr(work)
        expected_result = 'Size: 3\nWorkers: Gogo, Emma'

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
