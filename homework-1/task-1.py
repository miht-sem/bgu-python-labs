def print_star_pyramid(pyramid_height: int):
    for i in range(pyramid_height):
        spaces = ' ' * (pyramid_height - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)


if __name__ == '__main__':
    while True:
        try:
            n = int(input("Enter the height of the triangle: "))
            break
        except ValueError:
            print('Invalid input, please write integer value.')
    print_star_pyramid(n)
