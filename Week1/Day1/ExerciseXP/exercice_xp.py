# Exercises XP

# Exercise 1 Hello World
print(f"Hello world\n" * 5)

# Exercise 2 Some Math
print(f"(99^3)*8 = {(99**3)*8}")

# Exercise 3 What is the output?
5 < 3 #False
3 == 3 #True
3 == "3" #False
"Hello" == "hello" #False


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


# Exercise 7: Odd or Even
n = int(input("saisissez un nombre : "))
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
t = int(input("donnez votre taille en centimetres svp : "))
if t > 145:
    print("vous êtes trop grand pour conduire")
else:
    print("vous avez besoin de grandir davantage avant de conduire")
