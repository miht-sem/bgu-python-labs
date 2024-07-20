def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def main():
    while True:
        try:
            first_num = int(input("Please enter first number: "))
            second_num = int(input("Please enter second number: "))
            break
        except ValueError:
            print('Invalid input, please enter an integer value.')
    print(gcd(a=first_num, b=second_num))


if __name__ == '__main__':
    main()
