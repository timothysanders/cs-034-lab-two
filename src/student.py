""""""

class Student:

    _student_data = {}

    def __init__(self, student_id: int, name: str):
        self._name = name
        self._id = student_id
        if student_id not in self._student_data:
            self._student_data[student_id] = {
                "name": name,
                "grades": {}  # Stores course codes and grades
            }

    def add_grade(self, course, grade): # Here "course" is an object of class Course
        """Updates a grade for a course"""
        self._student_data[self._id]["grades"][course.get_course_code()] = {"grade": grade, "credits": course.get_credits()}


    def get_grades(self):
        """Retrieves student's grades"""
        return self._student_data[self._id]["grades"]

    def get_info(self):
        """Retrieves complete student information"""
        return self._student_data.get(self._id, "Student not found")

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_average(self):
        total_score = 0
        total_credits = 0
        overall_letter_grade = "F"
        overall_gpa = 0.0
        for _, grade in self.get_grades().items():
            total_score += grade["grade"] * grade["credits"]
            total_credits += grade["credits"]
        average_score = total_score / total_credits
        if average_score >= 97:
            overall_letter_grade = "A+"
            overall_gpa = 4.0
        elif average_score >= 93:
            overall_letter_grade = "A"
            overall_gpa = 4.0
        elif average_score >= 90:
            overall_letter_grade = "A-"
            overall_gpa = 3.7
        elif average_score >= 87:
            overall_letter_grade = "B+"
            overall_gpa = 3.3
        elif average_score >= 83:
            overall_letter_grade = "B"
            overall_gpa = 3.0
        elif average_score >= 80:
            overall_letter_grade = "B-"
            overall_gpa = 2.7
        elif average_score >= 77:
            overall_letter_grade = "C+"
            overall_gpa = 2.3
        elif average_score >= 73:
            overall_letter_grade = "C"
            overall_gpa = 2.0
        elif average_score >= 70:
            overall_letter_grade = "C-"
            overall_gpa = 1.7
        elif average_score >= 67:
            overall_letter_grade = "D+"
            overall_gpa = 1.3
        elif average_score >= 65:
            overall_letter_grade = "D"
            overall_gpa = 1.0
        return {"calculated_letter_grade": overall_letter_grade, "calculated_gpa": overall_gpa}


    def __str__(self):
        """Return a formatted string representation of the given student"""
        if self.get_grades() == {}:
            string_message = f"Student: {self._name} (ID: {self._id} | Overall Grade: N/A | Overall GPA: N/A)"
        else:
            results = self.get_average()
            string_message = f"Student: {self._name} (ID: {self._id} | Overall Grade: {results["calculated_letter_grade"]} | Overall GPA: {results["calculated_gpa"]})"
        return string_message

