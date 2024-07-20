import re


def read_strings_from_file() -> list[str]:
    strings = []
    try:
        with open("input.txt", "r") as f:
            strings = f.readlines()
    except FileNotFoundError:
        print("Input file not found.")
    return strings


def write_results_to_file(strings: list[str]) -> None:
    with open("output.txt", "w") as f:
        for string in strings:
            f.write(f"{string}\n")


def is_str_balance(string: str) -> str:
    stack = []
    matching_bracket = {')': '(', '}': '{', ']': '[', '>': '<'}

    for char in string:
        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching_bracket.keys():
            if not stack or stack.pop() != matching_bracket[char]:
                return 'false'

    return 'true' if not stack else 'false'


def determine_strings_balance() -> None:
    try:
        strings = read_strings_from_file()
        is_balance_strings = [is_str_balance(string) for string in strings]
        write_results_to_file(is_balance_strings)
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    determine_strings_balance()


if __name__ == '__main__':
    main()
