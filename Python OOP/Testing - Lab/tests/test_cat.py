from unittest import TestCase, main

from projects.cat import Cat


class CatTests(TestCase):
    def test_init_is_initialized_correctly(self):
        cat = Cat("Piss")

        self.assertEqual("Piss", cat.name)
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)
        self.assertEqual(0, cat.size)

    def test_eat_if_already_fed_raises(self):
        cat = Cat("Piss")

        cat.eat()

        with self.assertRaises(Exception) as ex:
            cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_eat_fed_changes_to_true_correctly(self):
        cat = Cat("Piss")

        cat.eat()

        self.assertTrue(cat.fed)

    def test_eat_sleepy_changes_to_true_correctly(self):
        cat = Cat("Piss")

        cat.eat()

        self.assertTrue(cat.sleepy)

    def test_eat_size_incremented_correctly(self):
        cat = Cat("Piss")

        cat.eat()

        self.assertEqual(1, cat.size)

    def test_sleep_if_already_fed_raises(self):
        cat = Cat("Piss")

        with self.assertRaises(Exception) as ex:
            cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_sleep_if_not_fed_sleepy_becomes_false_correctly(self):
        cat = Cat("Piss")

        self.assertFalse(cat.sleepy)

        cat.eat()

        self.assertTrue(cat.sleepy)

        cat.sleep()

        self.assertFalse(cat.sleepy)


if __name__ == "__main__":
    main()
