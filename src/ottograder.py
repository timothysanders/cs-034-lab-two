"""
Class and method definitions for the OttoGrader class

The OttoGrader class allows for the management of student and course (credit and non-credit) objects.
Student objects can be associated with one or more Course objects and Course objects can be
associated with one or more Student objects.
"""
from src.course import CreditCourse, NonCreditCourse
from src.student import Student

class OttoGrader:
    def __init__(self):
        """Constructor for OttoGrader object"""
        self._students = {}
        self._courses = {}

    def add_student(self, student_name: str, student_identifier: int):
        """
        Add a new student to the grader instance.

        Parameters
        ----------
        student_name : str
        student_identifier : int

        Returns
        -------
        None
        """
        new_student = Student(student_name, student_identifier)
        self._students[new_student.get_id()] = new_student

    def get_students(self):
        """
        Displays the currently enrolled students.

        Returns
        -------

        """
        return self._students

    def add_course(self, course_code: str, course_name: str, credits: int = 0):
        """
        Add a new course to the grader instance.

        If the number of credits is not specified or is zero, a non-credit course will be added. Otherwise,
        a credit course is added.

        Parameters
        ----------
        course_code : str
        course_name : str
        credits : int

        Returns
        -------
        None
        """
        if credits > 0:
            new_course = CreditCourse(course_code, course_name, credits)
        else:
            new_course = NonCreditCourse(course_code, course_name)
        self._courses[new_course.get_course_code()] = new_course

    def get_courses(self):
        return self._courses

    def add_student_to_course(self, student_id, course_code: str):
        """
        Add a student to a course based on either their name or identifier.

        Parameters
        ----------
        student_id
        course_id

        Returns
        -------

        """
        if course_code not in self._courses:
            raise ValueError(f"Course {course_code} does not exist")
        if student_id not in self._students:
            raise ValueError(f"Student {student_id} does not exist")
        self._courses[course_code].add_student(student_id)

    def get_course(self, course_code):
        return self._courses.get(course_code)
    def get_student(self, student_id):return self._students.get(student_id)
    def record_grade(self, student_id, course_name, grade):
        course = self.get_course(course_name)
        if course:
            student = course.get_student(student_id)
            if student:
                student.add_grade(course_name, grade)
            else:
                print(f"Student with ID {student_id} not found in {course_name}")
        else:
            print(f"Course {course_name} not found")
