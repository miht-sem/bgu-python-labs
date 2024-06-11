def read_marks_from_file() -> list[tuple[str, int]]:
    student_marks = []
    try:
        with open("input.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                try:
                    name, mark = map(str.strip, line.split(","))
                    student_marks.append((name, int(mark)))
                except ValueError:
                    print(f"Error parsing line: {line.strip()}")
    except FileNotFoundError:
        print("Input file not found.")
    return student_marks


def write_names_in_file(student_marks: list[tuple[str, int]], average_mark: float) -> None:
    with open("output.txt", "w") as f:
        for student, mark in student_marks:
            if mark > average_mark:
                f.write(f"{student}\n")


def average_mark_of_students() -> None:
    try:
        student_marks = read_marks_from_file()
        num_of_students = len(student_marks)
        if num_of_students > 0:
            total_marks = sum(map(lambda x: x[1], student_marks))
            average = total_marks / num_of_students
            write_names_in_file(student_marks, average)
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    average_mark_of_students()


if __name__ == '__main__':
    main()
