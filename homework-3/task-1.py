def read_cities_from_file() -> list[tuple[str, int]]:
    cities_population = []
    try:
        with open("cities.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                try:
                    city, population = map(str.strip, line.split(":"))
                    cities_population.append((city, int(population)))
                except ValueError:
                    print(f"Error parsing line: {line.strip()}")
    except FileNotFoundError:
        print("Input file not found.")
    return cities_population


def write_cities_to_file(cities_population: list[tuple[str, int]]) -> None:
    with open("filtered_cities.txt", "w") as f:
        for city, population in cities_population:
            f.write(f"{city}:{population}\n")


def filter_cities_from_file(min_population: int) -> None:
    try:
        cities_population = read_cities_from_file()
        filtered_cities_population = [
            city for city in cities_population if city[1] > min_population
        ]
        filtered_cities_population.sort(key=lambda city: city[0])
        write_cities_to_file(filtered_cities_population)
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    while True:
        try:
            min_population = int(input("Please enter the minimum number of population: "))
            break
        except ValueError:
            print('Invalid input, please enter an integer value.')
    filter_cities_from_file(min_population)


if __name__ == '__main__':
    main()
