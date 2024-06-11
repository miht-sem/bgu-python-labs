def read_lines_from_files(filenames: list[str]) -> list[str]:
    all_lines = []
    for filename in filenames:
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
                all_lines.extend([line.rstrip('\n') for line in lines])
        except FileNotFoundError:
            print(f"File {filename} not found.")
    return all_lines


def write_lines_to_file(lines: list[str], output_filename: str) -> None:
    with open(output_filename, "w") as f:
        for line in sorted(lines):
            f.write(f"{line}\n")


def main() -> None:
    input_files = ["input1.txt", "input2.txt"]
    output_file = "output.txt"

    all_lines = read_lines_from_files(input_files)
    write_lines_to_file(all_lines, output_file)


if __name__ == '__main__':
    main()
