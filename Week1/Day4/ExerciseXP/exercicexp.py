# Exercise 1: Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Step 1: Create the Siamese class
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Step 2: Create a list of cat instances
bengal_obj = Bengal('Luna', 3)
chartreux_obj = Chartreux('Milo', 5)
siamese_obj = Siamese('Nala', 2)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

# Step 3: Create a Pets instance
sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
sara_pets.walk()



# Exercise 2: Dogs

# Step 1: Create the Dog class
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f'{self.name} won the fight against {other_dog.name}!'
        elif other_power > my_power:
            return f'{other_dog.name} won the fight against {self.name}!'
        else:
            return f'{self.name} and {other_dog.name} tied!'


# Step 2: Create dog instances
dog1 = Dog('Rex', 3, 30)
dog2 = Dog('Bella', 5, 20)
dog3 = Dog('Max', 2, 25)

# Step 3: Test dog methods
print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(dog1.run_speed())
print(dog2.run_speed())
print(dog3.run_speed())

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog1.fight(dog3))


# Exercise 3: Dogs Domesticated

import random
from dog import Dog          


class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = [self.name] + [dog.name for dog in args]
        print(f"{', '.join(dog_names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs",
                      "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet!")


# Tests
fido  = PetDog("Fido",  2, 10)
buddy = PetDog("Buddy", 3, 15)
max_  = PetDog("Max",   4, 20)

print("--- Train ---")
fido.train()

print("\n--- Play ---")
fido.play(buddy, max_)

print("\n--- Do a trick (trained) ---")
fido.do_a_trick()

print("\n--- Do a trick (not trained) ---")
buddy.do_a_trick()

print("\n--- Inherited methods still work ---")
print(fido.run_speed())
print(fido.fight(buddy))

# 🌟 Exercise 4: Family and Person Classes


# Step 1: Create the Person class
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


# Step 2: Create the Family class
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)
        print(f"Welcome to the family, {first_name} {self.last_name}!")

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents Jane and John accept "
                          f"that you will go out with your friends")
                else:
                    print(f"Sorry, you are not allowed to go out with your friends.")
                return
        print(f"{first_name} is not a member of the {self.last_name} family.")

    def family_presentation(self):
        print(f"\n--- The {self.last_name} Family ---")
        for member in self.members:
            print(f"  {member.first_name} {member.last_name}, age {member.age}")


# --- Tests ---
family = Family("Johnson")

family.born("Alice", 22)
family.born("Tom", 15)
family.born("Emma", 18)

family.family_presentation()

print("\n--- Majority Checks ---")
family.check_majority("Alice")
family.check_majority("Tom")
family.check_majority("Emma")
family.check_majority("Lucas")