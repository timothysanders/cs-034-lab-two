""""""

class Student:
    """
    Manages student information with grade storage

    Attributes
    ----------
    _id : str
        The unique identifier for a given student.
    _name : str
        The full name of a given student.
    _student_data : a class dict
        Dictionary to store {student_id: {"name": name, "grades": {course_code: grade}} for all enrolled students.

    Methods
    -------
    add_grade(course, grade)
        Update grade for a given course.
    get_grades()
        Retrieve grades for a given student
    ?? get_info(): seems redundant method compared to the method "__str__(self)"
        Retrieve a given student's info
    get_name():
        Retrieve a given student's name.
    get_id():
        Retrieve a given student's ID.
    get_average():
        Return a letter grade and GPA for a given student
    _convert_score_to_grade():
        Convert a score into a letter grade and GPA.
    __str__()
        ??? String representation for a Student object, the method "get_info" seems redundant
    """

    _student_data = {}

    def __init__(self, student_id: int, name: str):
        self._name = name
        self._id = student_id
        if student_id not in self._student_data:
            self._student_data[student_id] = {
                "name": name,
                "grades": {}  # Stores course codes and grades
            }

    def add_grade(self, course, grade: float) -> None: # Here "course" is an object of class Course
        """
        Updates grade for a given course.

        Parameters
        ----------
        course : Course
        grade : float

        Returns
        -------
        None
        """
        self._student_data[self._id]["grades"][course.get_course_code()] = {"grade": grade, "credits": course.get_credits()}


    def get_grades(self):
        """
        Retrieve student's grades from courses that have assigned a grade.

        Returns
        -------
        dict
            A dictionary containing graded courses.
        """
        return self._student_data[self._id]["grades"]

    def get_info(self):
        """Retrieves complete student information"""
        return self._student_data.get(self._id, "Student not found")

    def get_name(self) -> str:
        """

        Returns
        -------
        str
            The student object's name.
        """
        return self._name

    def get_id(self) -> int:
        """
        Retrieve the student object's ID.

        Returns
        -------
        int
            The student ID.
        """
        return self._id

    def get_average(self) -> dict:
        """
        Calculate the average score in classes, weighted by credits.

        Returns
        -------
        dict
            A dictionary containing the calculated letter grade and GPA
        """
        total_score = 0
        total_credits = 0
        for _, grade in self.get_grades().items():
            total_score += grade["grade"] * grade["credits"]
            total_credits += grade["credits"]
        average_score = total_score / total_credits
        return self._convert_score_to_grade(average_score)

    def _convert_score_to_grade(self, score: float) -> dict:
        """
        Convert a score into a letter grade and GPA.

        Parameters
        ----------
        score : float

        Returns
        -------
        dict
            A dictionary containing the calculated letter grade and GPA
        """
        grade_scale = ([
            (97, "A+", 4.0),
            (93, "A", 4.0),
            (90, "A-", 3.7),
            (87, "B+", 3.3),
            (83, "B", 3.0),
            (80, "B-", 2.7),
            (77, "C+", 2.3),
            (73, "C", 2.0),
            (70, "C-", 1.7),
            (67, "D+", 1.3),
            (65, "D", 1.0),
            (0, "F", 0.0)
        ])
        for min_score, letter_grade, gpa in grade_scale:
            if score >= min_score:
                return {"calculated_letter_grade": letter_grade, "calculated_gpa": gpa}


    def __str__(self):
        """Return a formatted string representation of the given student"""
        if self.get_grades() == {}:
            string_message = f"Student: {self._name} (ID: {self._id} | Overall Grade: N/A | Overall GPA: N/A)"
        else:
            results = self.get_average()
            string_message = f"Student: {self._name} (ID: {self._id} | Overall Grade: {results["calculated_letter_grade"]} | Overall GPA: {results["calculated_gpa"]})"
        return string_message
