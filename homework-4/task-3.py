def count_ways_to_get_up(n) -> int:
    a = 1
    b = 1
    for _ in range(n - 1):
        a, b = b, a + b  # Fibonacci :)
    return a


def main():
    while True:
        try:
            n = int(input("Please enter number of steps: "))
            break
        except ValueError:
            print('Invalid input, please enter an integer value.')
    print(count_ways_to_get_up(n))


if __name__ == '__main__':
    main()
