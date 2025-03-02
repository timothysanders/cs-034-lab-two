"""
Tests for CreditCourse and NonCreditCourse classes.

Tests can be run by installing pytest and running `pytest .` from the repo root.
"""
import pytest
from src.course import CreditCourse, NonCreditCourse
from src.student import Student

@pytest.fixture
def student():
    """Fixture to create a sample student."""
    return Student(123, "Alice")

@pytest.fixture
def credit_course():
    """Fixture to create a sample CreditCourse."""
    return CreditCourse("CS001", "Introduction to Computers and Programming", 3)

@pytest.fixture
def non_credit_course():
    """Fixture to create a sample NonCreditCourse."""
    return NonCreditCourse("OLAD2900", "Sewing Techniques for Older Adults")

class TestCreditCourse:
    """Tests for the CreditCourse class."""

    def test_credit_course_creation(self, credit_course):
        """Test that a CreditCourse object is created correctly."""
        assert credit_course._course_code == "CS001"
        assert credit_course._course_name == "Introduction to Computers and Programming"
        assert credit_course.credits == 3
        assert credit_course._students == {}

    def test_credit_course_str(self, credit_course):
        """Test the __str__ method of CreditCourse."""
        expected_string = "CS001: Introduction to Computers and Programming (3 credit course, 0 student(s) enrolled)"
        assert str(credit_course) == expected_string

    def test_credit_course_add_student(self, credit_course, student):
        """Test adding a student to a CreditCourse."""
        credit_course.add_student(student)
        assert student.get_id() in credit_course._students
        assert credit_course._students[student.get_id()]["grade"] is None

    def test_credit_course_add_grade(self, credit_course, student):
        """Test adding a grade to a student in a CreditCourse."""
        credit_course.add_student(student)
        credit_course.add_grade(student, 90.0)
        assert credit_course._students[student.get_id()]["grade"] == 90.0
        assert student.get_grades()["CS001"]["grade"] == 90.0

    def test_credit_course_get_student_grade(self, credit_course, student):
        """Test retrieving a student's grade from a CreditCourse."""
        credit_course.add_student(student)
        credit_course.add_grade(student, 85.0)
        assert credit_course.get_student_grade(student) == 85.0

    def test_credit_course_get_student_grade_not_enrolled(self, credit_course, student):
        """Test retrieving a grade for a student not enrolled in CreditCourse."""
        with pytest.raises(ValueError) as excinfo:
            credit_course.get_student_grade(student)
        assert str(excinfo.value) == f"Student {student.get_name()} is not enrolled in {credit_course._course_name}."

    def test_get_course_code(self, credit_course):
        """Test the get_course_code method of CreditCourse."""
        assert credit_course.get_course_code() == "CS001"


class TestNonCreditCourse:
    """Tests for the NonCreditCourse class."""

    def test_non_credit_course_creation(self, non_credit_course):
        """Test that a NonCreditCourse object is created correctly."""
        assert non_credit_course._course_code == "OLAD2900"
        assert non_credit_course._course_name == "Sewing Techniques for Older Adults"
        assert non_credit_course._students == {}

    def test_non_credit_course_str(self, non_credit_course):
        """Test the __str__ method of NonCreditCourse."""
        expected_string = "OLAD2900: Sewing Techniques for Older Adults (non-credit course, 0 student(s) enrolled)"
        assert str(non_credit_course) == expected_string

    def test_non_credit_course_add_student(self, non_credit_course, student):
        """Test adding a student to a NonCreditCourse."""
        non_credit_course.add_student(student)
        assert student.get_id() in non_credit_course._students
        assert non_credit_course._students[student.get_id()]["grade"] is None

    def test_non_credit_course_add_grade(self, non_credit_course, student):
        """Test adding a grade to a student in a NonCreditCourse."""
        non_credit_course.add_student(student)
        non_credit_course.add_grade(student, 90.0)
        assert non_credit_course._students[student.get_id()]["grade"] == 90.0
        assert student.get_grades()["OLAD2900"]["grade"] == 90.0

    def test_non_credit_course_get_student_grade(self, non_credit_course, student):
        """Test retrieving a student's grade from a NonCreditCourse."""
        non_credit_course.add_student(student)
        non_credit_course.add_grade(student, 85.0)
        assert non_credit_course.get_student_grade(student) == 85.0

    def test_non_credit_course_get_student_grade_not_enrolled(self, non_credit_course, student):
        """Test retrieving a grade for a student not enrolled in NonCreditCourse."""
        with pytest.raises(ValueError) as excinfo:
            non_credit_course.get_student_grade(student)
        assert str(excinfo.value) == f"Student {student.get_name()} is not enrolled in {non_credit_course._course_name}."

    def test_get_course_code(self, non_credit_course):
        """Test the get_course_code method of NonCreditCourse."""
        assert non_credit_course.get_course_code() == "OLAD2900"