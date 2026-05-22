class Farm:
    # Step 2: L'initialisation
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}  

    # Step 3: Ajouter un animal (avec une valeur par défaut de 1 pour count)
    
    def add_animal(self, animal_type=None, count=1, **multiple_animals):
        # 1. On gère le cas classique (si on a passé un animal_type manuellement)
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

    # Step 4: Récupérer les informations complètes
    def get_info(self):
        
        info = f"{self.name}'s farm\n"
        
        
        for animal, quantity in self.animals.items():
            info += f"{animal} : {quantity}\n"
            
        
        info += "    E-I-E-I-0!"
        return info

    # Step 6 (Bonus): Liste triée des types d'animaux
    def get_animal_types(self):
        # sorted() renvoie une copie triée des clés du dictionnaire
        return sorted(self.animals.keys())

    # Step 7 (Bonus): Version courte du résumé (avec pluriels en "s")
    def get_short_info(self):
        
        types_tries = self.get_animal_types()
        
        liste_pluriels = []
        for animal in types_tries:
            
            if self.animals[animal] > 1:
                liste_pluriels.append(animal + "s")
            else:
                liste_pluriels.append(animal)
                
        debut = ", ".join(liste_pluriels[:-1])  # "cows, goats"
        dernier = liste_pluriels[-1]             # "sheeps"
        
        return f"{self.name}’s farm has {debut} and {dernier}."



# Step 5: Test du code (sans le Step 8 pour l'instant)

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')  # Ajoute 1 par défaut
macdonald.add_animal('sheep')  # Ajoute encore 1 (total 2)
macdonald.add_animal('goat', 12)

# Test du Step 4 & 5
print(macdonald.get_info())

# Test du Step 7 (Bonus)
print("\n" + macdonald.get_short_info())

# Test du Step 8
macdonald.add_animal(cow=5, sheep=2, goat=12)