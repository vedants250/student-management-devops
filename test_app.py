"""Unit tests for the Student Management System."""
import unittest

from app import (
    add_student,
    find_student,
    get_students,
    students,
    validate_email,
)


class TestStudentManagement(unittest.TestCase):
    def setUp(self):
        students.clear()

    def test_add_student(self):
        student = add_student(1, "Rahul", "AI & DS")
        self.assertEqual(student["name"], "Rahul")
        self.assertEqual(student["course"], "AI & DS")
        self.assertIsNone(student["email"])

    def test_find_student(self):
        add_student(2, "Priya", "Computer Engineering")
        student = find_student(2)
        self.assertIsNotNone(student)
        self.assertEqual(student["name"], "Priya")

    def test_student_not_found(self):
        self.assertIsNone(find_student(99))

    def test_get_students_returns_all_students(self):
        add_student(1, "Rahul", "AI & DS")
        add_student(2, "Priya", "Computer Engineering")
        self.assertEqual(len(get_students()), 2)

    def test_reject_empty_name(self):
        with self.assertRaises(ValueError):
            add_student(1, "  ", "AI & DS")

    def test_reject_duplicate_id(self):
        add_student(1, "Rahul", "AI & DS")
        with self.assertRaises(ValueError):
            add_student(1, "Another Student", "Computer Engineering")

    def test_email_validation_accepts_valid_email(self):
        validate_email("student@example.com")

    def test_email_validation_rejects_invalid_email(self):
        with self.assertRaises(ValueError):
            validate_email("not-an-email")

    def test_add_student_with_email(self):
        student = add_student(3, "Asha", "AI & DS", "asha@example.com")
        self.assertEqual(student["email"], "asha@example.com")


if __name__ == "__main__":
    unittest.main(verbosity=2)
