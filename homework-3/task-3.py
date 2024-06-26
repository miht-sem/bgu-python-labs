def read_courses_from_file(file_path: str = "input.txt") -> dict:
    students_courses = {}
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.strip():
                    student_data = line.split(":")
                    if len(student_data) == 2:
                        student_name = student_data[0].strip()
                        student_courses = student_data[1].strip(' ,.\n\t')
                        courses = [course.strip() for course in student_courses.split(",")]
                        students_courses[student_name] = courses
                    else:
                        print(f"Error parsing line: {line.strip()}")
    except FileNotFoundError:
        print("Input file not found.")
    return students_courses


def get_students_for_course(students_courses: dict, course_name: str) -> list:
    enrolled_students = [student for student, courses in students_courses.items() if course_name in courses]
    return enrolled_students


def main():
    students_courses = read_courses_from_file()
    course_name = input("Please enter the course name: ").strip()
    students = get_students_for_course(students_courses, course_name)

    if students:
        print(f"Students enrolled in {course_name}: {', '.join(students)}")
    else:
        print(f"No students are enrolled in {course_name}")


if __name__ == '__main__':
    main()
