class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}  

    def add_animal(self, animal_type=None, count=1, **multiple_animals):
        """Add one animal type at a time or several types with keyword arguments.

        Examples:
        - add_animal('cow', 3)
        - add_animal(cow=3, sheep=2)
        """
        if animal_type is not None:
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count
                
        
        for animal, quantity in multiple_animals.items():
            if animal in self.animals:
                self.animals[animal] += quantity
            else:
                self.animals[animal] = quantity

    def get_info(self):
        info = f"{self.name}'s farm\n"
        for animal, quantity in self.animals.items():
            info += f"{animal} : {quantity}\n"
        info += "    E-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()

        if not animal_types:
            return f"{self.name}'s farm has no animals."

        animal_list = []
        for animal in animal_types:
            if self.animals[animal] > 1:
                animal_list.append(animal + "s")
            else:
                animal_list.append(animal)

        if len(animal_list) == 1:
            return f"{self.name}'s farm has {animal_list[0]}."

        all_but_last = ", ".join(animal_list[:-1])
        last = animal_list[-1]
        return f"{self.name}'s farm has {all_but_last} and {last}."



macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')  # Ajoute 1 par défaut
macdonald.add_animal('sheep')  # Ajoute encore 1 (total 2)
macdonald.add_animal('goat', 12)

print(macdonald.get_info())

print("\n" + macdonald.get_short_info())

macdonald.add_animal(cow=5, sheep=2, goat=12)