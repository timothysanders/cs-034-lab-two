# cs-034-lab-two
Implementation of "Otto Grader"-- a student grade manage system

## Purpose
- Enroll a new student to a given course
- Update the record of a student’s grades

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
  
- Apply Inheritance and Abstraction when we implement the abstract base class Course and its derived child classes
  CreditCourse and NoncreditCourse

- The abstract base class Course outlines the needed abstract methods for its derived classes NoncreditCourse
  and CreditCourse. When it comes to the concrete implementation for these methods, we are applying the principle
  of Polymorphism to redefine or overload these abstract methods for NoncreditCourse and CreditCourse respectively


## Running the code
To run the code for the Otto Grader application, simply run the following command
```commandline
python main.py
```

## Running tests
<tbd>
