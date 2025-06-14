''' ZADANIE 1
Na podstawie podanej listy stwórz listę zawierającą same palindromy.
'''

slowa = ["ala", "kot", "pies", "kamilslimak", "zebra", "madam", "Adam"]
palindromy = [slowo for slowo in slowa if slowo == slowo[::-1]]
print(palindromy)

''' ZADANIE 2
Na podstawie listy krotek zawierającej długości boków trójkąta stwórz listę
zawierającą tylko krotki z których można skonstruować trójkąt.
'''

trojkaty = [(1, 3, 5), (2, 2, 3), (3, 1, 8), (3, 4, 5)]
# v1 - sprawdzamy wszystkie ścianki
poprawne_trojkaty = [trojkat for trojkat in trojkaty if trojkat[2] < trojkat[0] + trojkat[1] and trojkat[0] < trojkat[1] + trojkat[2] and trojkat[1] < trojkat[2] + trojkat[0]]
# v2 - sprawdzamy tylko największą
poprawne_trojkaty = [trojkat for trojkat in trojkaty if max(trojkat) < sum(trojkat) - max(trojkat)]

print(poprawne_trojkaty)

''' ZADANIE 3
Na podstawie listy z temperaturą podaną w stopniach Fahrenhaita stwórz
listę zawierającą te same temperatury w stopniach
Celcjusza
'''

stopnie_fahrenheit = [32, 68, 104, 140]


''' ZADANIE 4
Z podanego ciągu znaków usuń znaki nie będące literami ani cyframi.
'''

string = "hello@123world!456"

bez_symboli = [char for char in string if char.isalpha()]
print(''.join(bez_symboli))

