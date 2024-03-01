text = "abcdefghijklmnop"

for letter in text:
    print(letter)

i = 0
while i < len(text): #text = chaine de caractere, categorie des container (contient des objet, ici des lettres). text[3], ca va envoyer la 4eme lettre
    print(text[i])
    i += 1

i= len(text) - 1 #fait l'alphabet a l'envers
while i >= 0:
    print(text[i])
    i -= 1

print()
i = 0
while i < len(text):
    print(text[len(text)-i-1], end="") #end="", ca veut dire que ici au lieu d'aller a la ligne il rajoute end, qui ici est rien donc il met l'alphabet sur une meme ligne.
    i += 1

