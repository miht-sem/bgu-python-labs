def sum_of_digits(n: int) -> int:
    return sum(int(digit) for digit in str(n))


def reduce_to_single_digit(n: int) -> int:
    while n >= 10:
        n = sum_of_digits(n)
    return n


if __name__ == '__main__':
    while True:
        try:
            number = input("Enter a number: ")
            if number.isdigit():
                number = int(number)
                print(reduce_to_single_digit(number))
                break
            else:
                print("The number must be an integer.")
        except ValueError:
            print('Invalid input, please enter an integer value.')
