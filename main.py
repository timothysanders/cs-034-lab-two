from src.ottograder import OttoGrader

if __name__ == "__main__":
    print("Welcome to OttoGrader!")
    main_grader = OttoGrader()
    main_grader.add_student("Megan", 1235)
    main_grader.add_student("Michael", 1236)
    main_grader.add_student("Tim", 1234)
    main_grader.add_course("CS-034", "Advanced Python", 3)
    print(main_grader.get_courses())