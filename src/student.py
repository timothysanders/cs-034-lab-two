""""""

class Student:

    def __init__(self, name: str, identifier: int, year: str = None, grades: str = None):
        self._name = name
        self._id = identifier
        self._year = year
        self._grades = grades

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def add_grade(self, course, grade):
        """Adds a valid grade for a given course"""
        try:
            if not isinstance(grade, (int or float)):
                raise ValueError("Grade must be a numerical value.")
            if not (0 <= grade <= 100):
                raise ValueError("Grade must be between 0 and 100.")

            self.__grades[course] = grade  # Store valid grade
            print(f"Grade {grade} added for {course}")

        except ValueError as e:
            print(f"Error: {e}")

    def get_grades(self):
        return self._grades

    def get_average(self):
        if not self._grades:
            return 0  # Return 0 if no grades are available
        return sum(self._grades.values()) / len(self._grades)

    def __str__(self):
        """Return a formatted string representation of the given student"""
        return f"Student: {self.__name} (ID: {self.__id} | Grades: {self.__grades})"

