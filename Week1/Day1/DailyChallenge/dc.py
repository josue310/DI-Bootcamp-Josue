# Challenge 1

number = int(input("donnez un nombre : "))
length = int(input("donnez une taille : "))
l = []
for i in range(1,length+1):
    c = number * i
    l.append(c)
print(l)

#Challenge 2

word = input("Saisissez un mot : ")

result = ""

for letter in word:
    # Ajouter la lettre seulement si elle est différente
    # de la dernière ajoutée
    if result == "" or letter != result[-1]:
        result += letter

print("Le mot final:", result)