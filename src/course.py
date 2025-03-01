from abc import ABC, abstractmethod

from src.student import Student


class Course(ABC):
    """
    Abstract class to represent a course.

    Attributes
    ----------
    _course_code : str
        The code associated with the course.
    _course_name : str
        The full name of the course.
    _students : dict
        Dictionary containing all students enrolled in this course.

    Methods
    -------
    get_course_code()
    add_student(student)
    add_grade(student, grade)
    get_student_grade(student)
    get_course_info()
        An abstract method to be implemented in subclasses.
    __str__()
        An abstract method to be implemented in subclasses.
    """

    def __init__(self, course_code: str, course_name: str):
        self._course_code = course_code
        self._course_name = course_name
        self._students = {}

    def get_course_code(self) -> str:
        """
        Return the course code.

        Returns
        -------
        str
        """
        return self._course_code

    def add_student(self, student: Student) -> None:
        """
        Enroll a student in the course.

        Parameters
        ----------
        student : Student

        Returns
        -------
        None
        """
        if student.get_id() not in self._students:
            self._students[student.get_id()] = {"grade": None}
            print(f"Student {student.get_id()} enrolled in {self._course_name}.")
        else:
            print(f"Student {student.get_id()} is already enrolled in {self._course_name}.")

    def add_grade(self, student: Student, grade: float) -> None:
        """
        Assign a grade to an enrolled student.

        Parameters
        ----------
        student : Student
        grade : float

        Returns
        -------
        None
        """
        if student.get_id() in self._students:
            student.add_grade(self, grade)  # Store grade in the current Student object
            self._students[student.get_id()]["grade"] = grade  # Sync with Course records
            print(f"Grade {grade} added for {student.get_name()} in {self._course_name}.")
        else:
            print(f"Student {student.get_name()} is not enrolled in {self._course_name}.")

    def get_student_grade(self, student: Student) -> float:
        """
        Retrieve a student's grade for a given course.

        Parameters
        ----------
        student : Student

        Returns
        -------
        float
        """
        if student.get_id() in self._students:
            return self._students[student.get_id()]["grade"]
        else:
            raise ValueError(f"Student {student.get_name()} is not enrolled in {self._course_name}.")

    @abstractmethod
    def get_course_info(self):
        pass

    @abstractmethod
    def __str__(self):
        """String representation of the course object."""
        pass



class CreditCourse(Course):
    def __init__(self, course_id, course_name, course_credits):
        super().__init__(course_id, course_name)
        self.credits = course_credits

    def get_course_info(self):
        pass

    def __str__(self):
        """String representation of the credit course."""
        return f"{self._course_code}: {self._course_name} ({self.credits} credit course, {len(self._students)} student(s) enrolled)"

class NonCreditCourse(Course):
    def __init__(self, course_id, course_name):
        super().__init__(course_id, course_name)
        self.credits = None

    def get_course_info(self):
        pass

    def __str__(self):
        """String representation of the non-credit course."""
        return f"{self._course_code}: {self._course_name} (non-credit course, {len(self._students)} student(s) enrolled)"


# Test cases
if __name__ == "__main__":
    print('Grade and course info for a student with only credit courses courses:')
    print('Grade and course info for a student with an noncredit courses:')