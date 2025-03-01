class Student:
    
    _student_data = {}  # Class-level dictionary to store student info

    def __init__(self, student_id, name):
        self._id = student_id
        if student_id not in self._student_data:
            self._student_data[student_id] = {
                "name": name,
                "grades": {}  # Stores course codes and grades
            }


    def add_grade(self, course, grade): # Here "course" is an object of class Course
        """Updates a grade for a course"""
        self._student_data[self._id]["grades"][course._code] = grade


    def get_grades(self):
        """Retrieves student's grades"""
        return self._student_data[self._id]["grades"]

    def get_info(self):
        """Retrieves complete student information"""
        return self._student_data.get(self._id, "Student not found")


# Example Usage
if __name__ == "__main__":
  pass

    
