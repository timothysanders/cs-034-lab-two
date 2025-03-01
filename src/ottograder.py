from src.course import CreditCourse, NonCreditCourse
from src.student import Student

class OttoGrader:
    def __init__(self):
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

    def add_student_to_course(self, student, course_name):
        course = self.get_course(course_name)
        if course:
            course.enroll_student(student)
        else:
            print(f"Course {course_name} not found.")

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
