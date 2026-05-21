# Exercises XP

# Exercise 1 Hello World
print(f"Hello world\n" * 4)

# Exercise 2 Some Math
print(f"(99^3)*8 = {(99**3)*8}")

# Exercise 3 What is the output?
5 < 3 #False
3 == 3 #True
3 == "3" #False
"Hello" == "hello" #False
# "3" > 3 #TypeError in Python 3 (str and int cannot be compared with >)


# Exercise 4 Your computer brand
computer_brand = "LENOVO"
print(f"I have a {computer_brand} computer.")


# Exercise 5: Your information
name = "KOUADIO"
age = 21
shoe_size = 44
info = f"Je m'appelle {name} et j'ai {age} ans. Je chausse du {shoe_size} et j'aime les films d'horreur."
print(info)

# Exercise 6: A & B
a = 17
b = 5
if a > b:
    print("Hello World")


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrée invalide. Veuillez saisir un nombre entier.")


# Exercise 7: Odd or Even
n = read_int("saisissez un nombre : ")
if n % 2 == 0:
    print(f"Le nombre {n} est pair")
else:
    print(f"Le nombre {n} est impair")
    
# Exercise 8: What’s your name?
myname = "Josué"
yourname = input("saisissez votre nom svp : ")
if myname == yourname:
    print(f" Hey {yourname}!, nous avons le même nom")
else:
    print("ahh dommage ! nous n'avons pas le même nom")
    
# Exercise 9: Tall enough to ride a roller coaster
t = read_int("donnez votre taille en centimetres svp : ")
if t > 145:
    print("Vous êtes assez grand pour monter sur les montagnes russes !")
else:
    print("Vous devez encore grandir un peu avant de monter sur les montagnes russes.")
