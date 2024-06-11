def read_lines_from_file() -> list[str]:
    try:
        with open("input.txt", "r") as f:
            lines = f.readlines()
        return [line.rstrip('\n') for line in lines]
    except FileNotFoundError:
        print("Input file not found.")
        return []


def remove_chars_and_reverse(lines: list[str], chars_to_remove: str) -> list[str]:
    chars_to_remove = chars_to_remove + ";"
    processed_lines = []
    for line in lines:
        stripped_line = line.rstrip(chars_to_remove)
        reversed_line = stripped_line[::-1]
        processed_lines.append(reversed_line)
    return processed_lines


def write_lines_to_file(lines: list[str]) -> None:
    with open("output.txt", "w") as f:
        for line in lines:
            f.write(f"{line}\n")


def main() -> None:
    lines = read_lines_from_file()
    if not lines:
        return

    chars_to_remove = input("Enter the characters to remove from the right end of each line: ")
    processed_lines = remove_chars_and_reverse(lines, chars_to_remove)
    write_lines_to_file(processed_lines)


if __name__ == '__main__':
    main()
