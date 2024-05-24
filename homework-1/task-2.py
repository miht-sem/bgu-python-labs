def number_to_words(n: int) -> str:
    ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать",
             "восемнадцать", "девятнадцать"]
    tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
            "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    if n == 0:
        return "ноль"

    words = []

    if n // 100 > 0:
        words.append(hundreds[n // 100])

    if 10 < n % 100 < 20:
        words.append(teens[n % 10])
    else:
        if n % 100 >= 10:
            words.append(tens[n % 100 // 10])
        if n % 10 > 0:
            words.append(ones[n % 10])

    return " ".join(words)


if __name__ == '__main__':
    while True:
        try:
            number = int(input("Enter a number from 1 to 999: "))
            if 1 <= number <= 999:
                print(number_to_words(number))
                break
            else:
                print("The number must be from 1 to 999.")
        except ValueError:
            print('Invalid input, please write integer value from 1 to 999.')
