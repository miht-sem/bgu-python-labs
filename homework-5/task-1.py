import random
from typing import List, Optional


class Animal:
    def __init__(self, name: str, size: int, food_type: List[str], habitat: str, lifespan: int, gender: str):
        self._name = name
        self._size = size
        self._food_type = food_type
        self._habitat = habitat
        self._lifespan = lifespan
        self._age = 0
        self._satiety = 100
        self._gender = gender
        self._life = True

    def age_one_unit(self):
        self._age += 1
        if self._age >= self._lifespan:
            self._life = False

    def set_satiety(self, satiety: int):
        self._satiety = max(0, min(100, satiety))

    def increase_satiety(self, satiety: int):
        self.set_satiety(self._satiety + satiety)

    def decrease_satiety(self, satiety: int):
        self.set_satiety(self._satiety - satiety)
        if self._satiety < 10:
            self._life = False

    def is_alive(self) -> bool:
        return self._life

    def get_name(self) -> str:
        return self._name

    def get_size(self) -> int:
        return self._size

    def get_food_type(self) -> List[str]:
        return self._food_type

    def get_habitat(self) -> str:
        return self._habitat

    def get_satiety(self) -> int:
        return self._satiety

    def get_gender(self) -> str:
        return self._gender

    def get_lifespan(self) -> int:
        return self._lifespan

    def __str__(self):
        return f"{self._name} (Age: {self._age}, Satiety: {self._satiety}%, Gender: {self._gender})"

    def __repr__(self):
        return self.__str__()


class Herbivore(Animal):
    def __init__(self, name: str, size: int, habitat: str, lifespan: int, gender: str):
        super().__init__(name, size, ["plant"], habitat, lifespan, gender)


class Carnivore(Animal):
    def __init__(self, name: str, size: int, food_type: List[str], habitat: str, lifespan: int, gender: str):
        super().__init__(name, size, food_type, habitat, lifespan, gender)


class Ecosystem:
    def __init__(self):
        self._plant_food = 1000
        self._animals = []
        self._time = 0

    def add_animal(self, animal: Animal):
        self._animals.append(animal)

    def increase_plant_food(self, amount: int):
        self._plant_food += amount

    def view_animals_info(self):
        print("======= Animal Info =======")
        for index, animal in enumerate(self._animals):
            print(f"{index}: {animal}")

    def reproduce(self, index_animal1: int, index_animal2: int):
        if index_animal1 >= len(self._animals) or index_animal2 >= len(self._animals):
            print("======= Reproduce Info =======")
            print("Invalid index for reproduction.")
            return

        animal1 = self._animals[index_animal1]
        animal2 = self._animals[index_animal2]

        if animal1.get_name() != animal2.get_name() or animal1.get_gender() == animal2.get_gender():
            print("======= Reproduce Info =======")
            print("Reproduction is impossible: individuals must be of the same species and different sexes.")
            return

        habitat_conditions = {
            'water': (10, 50, 23),
            'air': (4, 42, 64),
            'earth': (2, 20, 73)
        }

        if animal1.get_habitat() in habitat_conditions:
            offspring_count, required_satiety, child_satiety = habitat_conditions[animal1.get_habitat()]
            if animal1.get_satiety() > required_satiety and animal2.get_satiety() > required_satiety:
                for _ in range(offspring_count):
                    new_animal = type(animal1)(
                        animal1.get_name(), animal1.get_size(), animal1.get_habitat(),
                        animal1.get_lifespan(), random.choice(['male', 'female'])
                    )
                    new_animal.set_satiety(child_satiety)
                    self.add_animal(new_animal)
                print("======= Reproduce Info =======")
                print(f"{offspring_count} {animal1.get_name()}(s) were created")

    def simulate_time(self):
        self._increase_ecosystem_age()
        eaten_animals = set()
        died_of_hunger = set()
        for animal in self._animals[:]:
            animal.age_one_unit()
            if not animal.is_alive() and animal not in eaten_animals:
                self._plant_food += animal.get_size()
                self._animals.remove(animal)
                continue

            if 'plant' in animal.get_food_type():
                if self._plant_food > 0:
                    self._plant_food -= 1
                    animal.increase_satiety(26)
                else:
                    animal.decrease_satiety(9)
            else:
                prey = self.find_prey(animal)
                if prey:
                    animal.increase_satiety(53)
                    eaten_animals.add(prey)
                    self._animals.remove(prey)
                else:
                    animal.decrease_satiety(16)

            if animal.get_satiety() < 10:
                died_of_hunger.add(animal)
                self._plant_food += animal.get_size()
                self._animals.remove(animal)
        self.__print_ecosystem_info(eaten_animals, died_of_hunger)

    def __print_ecosystem_info(self, eaten_animals, died_of_hunger):
        print("======= Ecosystem Info =======")
        print(f"Plant Food: {self._plant_food}")
        print("Animals:", *self._animals)
        print(
            f"{'Eaten Animals ' + str(len(eaten_animals)) + ': ' + 
               ', '.join(map(str, eaten_animals)) if eaten_animals else 'No animals were eaten'}")
        print(
            f"{'Animals Died of Hunger ' + str(len(died_of_hunger)) + ': ' + 
               ', '.join(map(str, died_of_hunger)) if died_of_hunger else 'No animals died from hunger'}")
        print(f"Ecosystem Age: {self._time}")

    def _increase_ecosystem_age(self):
        self._time += 1

    def find_prey(self, predator: Animal) -> Optional[Animal]:
        prey_list = [a for a in self._animals if a.get_name() in predator.get_food_type()]
        return random.choice(prey_list) if prey_list else None


def main():
    ecosystem = Ecosystem()

    species_list = [
        Carnivore("Lion", 200, ["Antelope", "Zebra"], "earth", 15, "male"),
        Carnivore("Lion", 200, ["Antelope", "Zebra"], "earth", 15, "female"),
        Herbivore("Antelope", 100, "earth", 10, "female"),
        Carnivore("Eagle", 20, ["Rabbit", "Mouse"], "air", 20, "male"),
        Herbivore("Rabbit", 10, "earth", 8, "female"),
        Carnivore("Shark", 500, ["Fish", "Seal"], "water", 30, "male"),
        Herbivore("Fish", 5, "water", 5, "female"),
        Herbivore("Zebra", 300, "earth", 25, "male"),
        Herbivore("Seal", 400, "water", 20, "female"),
        Herbivore("Mouse", 1, "earth", 3, "male"),
        Herbivore("Turtle", 100, "water", 100, "female"),
        Herbivore("Turtle", 100, "water", 100, "male"),
        Carnivore("Hawk", 15, ["Mouse"], "air", 18, "male"),
        Herbivore("Parrot", 1, "air", 50, "female")
    ]

    for species in species_list:
        ecosystem.add_animal(species)

    print("Welcome to the Ecosystem Simulator!")
    print("Initial animal info:")
    ecosystem.view_animals_info()

    def show_help():
        print("\nAvailable commands:")
        print("add_animal - Add an animal to the ecosystem")
        print("increase_plant_food - Increase the plant food on the planet")
        print("view_animals_info - View current characteristics of each animal")
        print("reproduce - Simulate the reproduction process of two animals of the same species and different sexes")
        print("simulate_time - Simulate the passage of time by one unit")
        print("help - Show this help message")
        print("exit - Exit the simulation\n")

    show_help()

    while True:
        command = input("Enter a command: ").strip().lower()

        if command == "add_animal":
            try:
                name = input("Enter the animal name: ").strip()
                size = int(input("Enter the animal size: ").strip())
                food_type = list(map(str.strip, input(
                    "Enter the animal food types (comma-separated food or 'plant' for herbivore): ").strip().split(',')))
                habitat = input("Enter the animal habitat: ").strip()
                lifespan = int(input("Enter the animal lifespan: ").strip())
                gender = input("Enter the animal gender (male/female): ").strip().lower()

                if 'plant' in food_type:
                    ecosystem.add_animal(Herbivore(name, size, habitat, lifespan, gender))
                else:
                    ecosystem.add_animal(Carnivore(name, size, food_type, habitat, lifespan, gender))
                print(f"Added {name} to the ecosystem.")
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter valid data.")

        elif command == "increase_plant_food":
            try:
                amount = int(input("Enter the amount of plant food to add: ").strip())
                ecosystem.increase_plant_food(amount)
                print(f"Increased plant food by {amount}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif command == "view_animals_info":
            ecosystem.view_animals_info()

        elif command == "reproduce":
            try:
                index1 = int(input("Enter the index of the first animal: ").strip())
                index2 = int(input("Enter the index of the second animal: ").strip())
                ecosystem.reproduce(index1, index2)
            except ValueError:
                print("Invalid input. Please enter valid indices.")

        elif command == "simulate_time":
            ecosystem.simulate_time()

        elif command == "help":
            show_help()

        elif command == "exit":
            print("Exiting the simulation. Goodbye!")
            break

        else:
            print("Unknown command. Type 'help' to see the list of available commands.")


if __name__ == "__main__":
    main()
