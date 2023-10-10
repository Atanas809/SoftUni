from unittest import TestCase, main

from projects.student import Student


class StudentTests(TestCase):
    def test_init_is_initialized_correctly_without_courses_passed(self):
        student = Student("Ivan")

        self.assertEqual("Ivan", student.name)
        self.assertEqual({}, student.courses)

    def test_init_is_initialized_correctly_with_courses_passed(self):
        student = Student("Ivan", {"Python OOP": ["homework", "break"]})

        self.assertEqual("Ivan", student.name)
        self.assertEqual({"Python OOP": ["homework", "break"]}, student.courses)

    def test_enroll_with_course_already_enrolled(self):
        student = Student("Ivan", {"Python OOP": ["homework", "break"]})

        result = student.enroll("Python OOP", ["sleep", "eat"])
        expected_result = "Course already added. Notes have been updated."

        self.assertEqual(expected_result, result)
        self.assertEqual({"Python OOP": ["homework", "break", "sleep", "eat"]}, student.courses)

    def test_enroll_course_note_is_y(self):
        student = Student("Ivan", {"Python OOP": ["homework", "break"]})

        result = student.enroll("Java", ["oop", "expressions"], "Y")
        expected_result = "Course and course notes have been added."

        self.assertEqual(expected_result, result)

        expected_courses = {"Python OOP": ["homework", "break"], "Java": ["oop", "expressions"]}
        self.assertEqual(expected_courses, student.courses)

    def test_enroll_course_note_is_empty_string(self):
        student = Student("Ivan", {"Python OOP": ["homework", "break"]})

        result = student.enroll("Java", ["oop", "expressions"], "")
        expected_result = "Course and course notes have been added."

        self.assertEqual(expected_result, result)

        expected_courses = {"Python OOP": ["homework", "break"], "Java": ["oop", "expressions"]}
        self.assertEqual(expected_courses, student.courses)

    def test_enroll_course_note_is_invalid_char(self):
        student = Student("Ivan", {"Python OOP": ["homework", "break"]})

        result = student.enroll("Java", ["oop", "expressions"], "N")
        expected_result = "Course has been added."

        self.assertEqual(expected_result, result)

        expected_courses = {"Python OOP": ["homework", "break"], "Java": []}
        self.assertEqual(expected_courses, student.courses)

    def test_add_notes_with_invalid_course_raises(self):
        student = Student("Ivan", {"Python OOP": ["homework", "break"]})

        with self.assertRaises(Exception) as ex:
            student.add_notes("Java", ["oop", "expressions"])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_with_valid_course(self):
        student = Student("Ivan", {"Python OOP": ["homework", "break"]})

        result = student.add_notes("Python OOP", "oop")
        expected_result = "Notes have been updated"

        self.assertEqual(expected_result, result)
        expected_courses = {"Python OOP": ['homework', 'break', 'oop']}
        self.assertEqual(expected_courses, student.courses)

    def test_leave_course_with_invalid_course_name_raises(self):
        student = Student("Ivan", {"Python OOP": ["homework", "break"]})

        with self.assertRaises(Exception) as ex:
            student.leave_course("Java")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_with_valid_course_name(self):
        student = Student("Ivan", {"Python OOP": ["homework", "break"], "Java": []})

        result = student.leave_course("Java")
        expected_result = "Course has been removed"

        self.assertEqual(expected_result, result)
        self.assertEqual({"Python OOP": ["homework", "break"]}, student.courses)


if __name__ == "__main__":
    main()
