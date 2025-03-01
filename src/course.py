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
        if student.get_id() not in self._students.keys():
            self._students[student.get_id()] = student
            print(f"Student {student.get_id()} enrolled in {self._course_name}.")
        else:
            print(f"Student {student.get_id()} is already enrolled in {self._course_name}.")

    def add_grade(self, student_id, grade):
        """Assign a grade to an enrolled student"""
        if student_id in self._students:
            student.add_grade(self._name, grade)  # Store grade in the current Student object
            self._students[student._id]["grade"] = grade  # Sync with Course records
            print(f"Grade {grade} added for {student._name} in {self._name}.")
        else:
            print(f"Student {student._name} is not enrolled in {self._name}.")

    def get_student_grade(self, student):
        """Retrieve a student's grade for a given course"""
        if student._id in self._students:
            return self._students[student._id]["grade"]
        return f"Student {student._name} is not enrolled in {self._name}."

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
        return f"Course: {self._name} ({self._code}, Credits: {self._credit}, Enrolled: {len(self._students)}) students"



class CreditCourse(Course):
    def __init__(self, course_id, course_name, course_credits):
        super().__init__(course_id, course_name)
        self.credits = course_credits


class NonCreditCourse(Course):
    def __init__(self, course_id, course_name):
        super().__init__(course_id, course_name)
        self.credits = None
# Test cases
if __name__ == "__main__":
    print('Grade and course info for a student with only credit courses courses:')
    print('Grade and course info for a student with an noncredit courses:')