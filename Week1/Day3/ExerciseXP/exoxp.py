# Exercice xp

#🌟 Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
# cat1 = create the object
cat1 = Cat("jommy",18)
cat2 = Cat("memou",2)
cat3 = Cat("papitou",1)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    # ... code to find and return the oldest cat ...
    if cat2.age > oldest.age:
        oldest = cat2
    elif cat3.age > oldest.age:
        oldest = cat3
    return oldest
# Step 3: Print the oldest cat's details

leplus_vieux = find_oldest_cat(cat1, cat2, cat3)
print(f"the oldest cat's details are\n Nom : {leplus_vieux.name}\n Age : {leplus_vieux.age}")



# 🌟 Exercise 2 : Dogs

# create the dog class
class Dog:
    def __init__(self,name,height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name} goes woof")
    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high !")

# Step 2: Create Dog Objects
davids_dog = Dog("david", 2)
sarahs_dog = Dog("sarah", 5)

# Step 3: Print Dog Details and Call Methods
print(f"the details of the first dog are : \n name : {davids_dog.name}\n height : {davids_dog.height}")
davids_dog.bark()
sarahs_dog.bark()

#Step 4: Compare Dog Sizes
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is tall than {sarahs_dog.name}")
else:
    print(f"{sarahs_dog.name} is tall than {davids_dog.name}")



#🌟 Exercise 3 : Who’s the song producer?
# Step 1: Create the Song Class

class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()




### 🌟 Exercise 4 : Afternoon at the Zoo
# Step 1: Define the Zoo Class

class Zoo():
    def __init__(self,zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    def add_animal(self, *new_animals): # On ajoute l'étoile
        for animal in new_animals: # On boucle sur tous les animaux reçus
            if animal not in self.animals:
                self.animals.append(animal)
            else:
                print(f"{animal} already exists in the list")
    def get_animals(self):
        if self.animals != []:
            print("all animals currently in the zoo are : ")
            for i in self.animals:
                print(i)
        else:
            print("No animals in the zoo")
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} is sold now")
        else:
            print(f"{animal_sold} doesn't exist in the zoo")
    
    def sort_animals(self):
        dic = {}
        self.animals.sort() # Les animaux sont triés par ordre alphabétique
        
        for i in self.animals:
            lettre = i[0] # On récupère la première lettre (ex: "B")
            
            # Si la lettre n'est pas encore une clé du dictionnaire, on la crée avec une liste vide
            if lettre not in dic:
                dic[lettre] = []
            
            # Maintenant qu'on est sûr que la liste existe, on ajoute l'animal dedans
            dic[lettre].append(i)
            
        return dic # On renvoie le dictionnaire à la fin
            
    def get_groups(self):
        # 1. On récupère le dictionnaire généré par la méthode précédente
        groupes = self.sort_animals()
        
        # 2. On boucle sur chaque groupe (lettre = clé, liste_animaux = valeur)
        for lettre, liste_animaux in groupes.items():
            # 3. On affiche au format demandé "Lettre: [Liste]"
            print(f"{lettre}: {liste_animaux}")
   
# step 2

brooklyn_safari = Zoo("Brooklyn Safari")

# step 3

brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Cougar")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()



