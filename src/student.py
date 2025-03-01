""""""

class Student:

    _student_data = {}

    def __init__(self, student_id: int, name: str):
        self._name = name
        self._id = student_id
        self._courses = []
        if student_id not in self._student_data:
            self._student_data[student_id] = {
                "name": name,
                "grades": {}  # Stores course codes and grades
            }

    def add_grade(self, course, grade): # Here "course" is an object of class Course
        """Updates a grade for a course"""
        self._student_data[self._id]["grades"][course.get_course_code()] = grade


    def get_grades(self):
        """Retrieves student's grades"""
        return self._student_data[self._id]["grades"]

    def get_info(self):
        """Retrieves complete student information"""
        return self._student_data.get(self._id, "Student not found")

    def add_course(self, course):
        self._courses.append(course)

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    #def add_grade(self, course, grade):
    #    """Adds a valid grade for a given course"""
    #    pass
        # try:
        #     if not isinstance(grade, (int, float)):
        #         raise ValueError("Grade must be a numerical value.")
        #     if not (0 <= grade <= 100):
        #         raise ValueError("Grade must be between 0 and 100.")

        #     self.__grades[course] = grade  # Store valid grade
        #     print(f"Grade {grade} added for {course}")

        # except ValueError as e:
        #     print(f"Error: {e}")

    # def get_grades(self):
    #     return self._grades

    def get_average(self):
        pass
        # if not self._grades:
        #     return 0  # Return 0 if no grades are available
        # return sum(self._grades.values()) / len(self._grades)

    def __str__(self):
        """Return a formatted string representation of the given student"""
        return f"Student: {self._name} (ID: {self._id} | Grades: N/A)"

