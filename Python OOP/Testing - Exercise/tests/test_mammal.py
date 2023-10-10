from unittest import TestCase, main

from projects.mammal import Mammal


class MammalTests(TestCase):
    def test_init_is_initialized_correctly(self):
        mammal = Mammal("Gogo", "Cat", "Meow")

        self.assertEqual("Gogo", mammal.name)
        self.assertEqual("Cat", mammal.type)
        self.assertEqual("Meow", mammal.sound)
        self.assertEqual("animals", mammal.get_kingdom())

    def test_test_make_sound_returns_correct_string(self):
        mammal = Mammal("Gogo", "Cat", "Meow")

        result = mammal.make_sound()
        expected_result = "Gogo makes Meow"

        self.assertEqual(expected_result, result)

    def test_info_returns_correct_string(self):
        mammal = Mammal("Gogo", "Cat", "Meow")

        result = mammal.info()
        expected_result = "Gogo is of type Cat"

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()