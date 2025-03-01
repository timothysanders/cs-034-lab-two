from src.student import Student


class Course:

    def __init__(self, course_code, course_name):
        self._course_code = course_code
        self._course_name = course_name
        self._students = {}

    def get_course_code(self):
        return self._course_code

    def add_student(self, student):
        """
        Enroll a student in the course.

        Parameters
        ----------
        student
        Returns
        -------
        None
        """
        if student.get_id() not in self._students:
            self._students[student.get_id()] = {"grade": None}
            print(f"Student {student.get_id()} enrolled in {self._course_name}.")
        else:
            print(f"Student {student.get_id()} is already enrolled in {self._course_name}.")

    def add_grade(self, student, grade):
        """Assign a grade to an enrolled student"""
        if student.get_id() in self._students:
            student.add_grade(self, grade)  # Store grade in the current Student object
            self._students[student.get_id()]["grade"] = grade  # Sync with Course records
            print(f"Grade {grade} added for {student.get_name()} in {self._course_name}.")
        else:
            print(f"Student {student.get_name()} is not enrolled in {self._course_name}.")

    def get_student_grade(self, student):
        """Retrieve a student's grade for a given course"""
        if student.get_id() in self._students:
            return self._students[student.get_id()]["grade"]
        return f"Student {student.get_name()} is not enrolled in {self._course_name}."

    def get_course_info(self):
        """Retrieve detailed course information"""
        enrolled_students = {
            student_dic["student"]._id: {"name": student["student"]._name, "grade": student["grade"]}
            for student_dic in self._students.values()
        }
        return {
            "Course Code": self._code,
            "Course Name": self._name,
            "Credit": self._credit,
            "Enrolled Students": enrolled_students
        }

    def __str__(self):
        """String representation of the course."""
        return f"Course: {self._course_code}-{self._course_name}, Enrolled: {len(self._students)}) students"



class CreditCourse(Course):
    def __init__(self, course_id, course_name, course_credits):
        super().__init__(course_id, course_name)
        self.credits = course_credits

    def __str__(self):
        """String representation of the credit course."""
        return f"{self._course_code}-{self._course_name}: {self.credits} credit course, Enrolled: {len(self._students)}) students"

class NonCreditCourse(Course):
    def __init__(self, course_id, course_name):
        super().__init__(course_id, course_name)
        self.credits = None

    def __str__(self):
        """String representation of the non-credit course."""
        return f"{self._course_code}-{self._course_name}: non-credit course, Enrolled: {len(self._students)}) students"


# Test cases
if __name__ == "__main__":
    print('Grade and course info for a student with only credit courses courses:')
    print('Grade and course info for a student with an noncredit courses:')