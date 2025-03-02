from src.ottograder import OttoGrader

if __name__ == "__main__":
    print("Welcome to OttoGrader!")
    main_grader = OttoGrader()
    main_grader.add_student("Megan", 1235)
    main_grader.add_student("Michael", 1236)
    main_grader.add_student("Tim", 1234)
    main_grader.add_course("CS034", "Advanced Python", 3)
    main_grader.add_course("CS003", "Intro Python", 3)
    main_grader.add_course("OLAD2900", "Sewing Techniques")
    main_grader.add_student_to_course(1234, "CS034")
    main_grader.add_student_to_course(1234, "CS003")
    main_grader.add_student_to_course(1234, "OLAD2900")
    main_grader.record_grade(1234, "CS034", 80)
    main_grader.record_grade(1234, "CS003", 100)
    main_grader.record_grade(1234, "OLAD2900", 50)
    main_grader.get_student_gpa(1234)