# cs-034-lab-two
Implementation of "Otto Grader"-- a student grade manage system

## Purpose
- Enroll a new student to a given course
- Update the record of a student’s grades
- Retrieve information for a given course
- Retrieve information for an enrolled student
- Calculate the average grade of a student
- GPA calculation for a student

## OttoGrader Grade Manage System Structure & Architecture
The code to run the Otto Grader application relies on the following classes


- Student
- Course
- CreditCourse (inherits from Course)
- NonCreditCourse (inherits from Course)
- OttoGrader

The entry point into the application is the `main.py` file, which handles the overall application logic

## Summary

By applying OOP principles (Encapsulation, Abstraction, Inheritance, and Polymorphism), we can better organize our
complicated student, course and grades data information, which not only  restricts unauthorized access to our data
but also is convenient for us to adapt and extend our codes for different scenarios in the future.

- Encapsulate each component (Student, Course, NoncreditCourse, CreditCourse, GradeManager) and its related
  operations in its respective class, making it easier to manage

- In our OOP OttoGrader, we pass objects of one class as parameters to the methods of another class, such as passing
  an object of Student to the method of “add_student()” for the class Course, or passing an object of Course to the
  method of “add_grade()” for the class Student. This enables us to interact with the passed object of a given class
  in its corresponding receiving class, which is a practice of encapsulation. Here, the principle of abstraction also
  works since the receiving class does not need to know the details of the passed object.
  
- The abstract base class Course outlines the needed abstract methods for its derived classes NoncreditCourse
  and CreditCourse. When it comes to the concrete implementation for these methods, we are applying the principle
  of Polymorphism to redefine or overload these abstract methods for NoncreditCourse and CreditCourse respectively

- Apply Inheritance and Abstraction when we implement the abstract base class Course and its derived child classes
  CreditCourse and NoncreditCourse


## Running the code
To run the code for the Otto Grader application, simply run the following command
```commandline
python main.py
```

## Running tests
<tbd>
