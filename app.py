"""Small in-memory Student Management System for Experiment 1."""
import re
from typing import Any

students: list[dict[str, Any]] = []


def validate_student(student_id: int, name: str, course: str) -> None:
    """Raise ValueError when the required student details are invalid."""
    if not isinstance(student_id, int) or student_id <= 0:
        raise ValueError("student_id must be a positive integer")
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name cannot be empty")
    if not isinstance(course, str) or not course.strip():
        raise ValueError("course cannot be empty")


def validate_email(email: str) -> None:
    """Basic email-format validation for this lab example."""
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    if not isinstance(email, str) or not re.fullmatch(pattern, email.strip()):
        raise ValueError("email address is invalid")


def add_student(
    student_id: int,
    name: str,
    course: str,
    email: str | None = None,
) -> dict[str, Any]:
    """Validate and add a student; IDs must be unique."""
    validate_student(student_id, name, course)
    if find_student(student_id) is not None:
        raise ValueError(f"student ID {student_id} already exists")
    if email is not None:
        validate_email(email)

    student = {
        "id": student_id,
        "name": name.strip(),
        "course": course.strip(),
        "email": email.strip() if email else None,
    }
    students.append(student)
    return student


def get_students() -> list[dict[str, Any]]:
    """Return a copy of the current student list."""
    return [student.copy() for student in students]


def find_student(student_id: int) -> dict[str, Any] | None:
    """Find a student by ID, returning None when not found."""
    for student in students:
        if student["id"] == student_id:
            return student.copy()
    return None


if __name__ == "__main__":
    students.clear()
    add_student(1, "Rahul", "AI & DS", "rahul@example.com")
    add_student(2, "Priya", "Computer Engineering", "priya@example.com")
    print("Student Management System")
    for item in get_students():
        print(item)
    print("Search for ID 1:", find_student(1))
