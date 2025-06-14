
lista = [1,2,3,4,5,6,7,8,9,10]

# 1 - kwadraty liczb
kwadraty = [i**2 for i in lista]
print(kwadraty)

# 2 - krotki, zbiory, słowniki
kwadraty = tuple(i**2 for i in lista)    # krotka
print(kwadraty)
kwadraty = {i**2 for i in lista}    # zbiór
print(kwadraty)
kwadraty = {i:i**2 for i in lista}  # słownik
print(kwadraty)

# 3 - zakresy
podwojenia = [2*i for i in range(3,6)]
print(podwojenia)

# 4 - warunki
parzyste = [i**2 for i in lista if i%2 == 0]
print(parzyste)

# 5 - łączenie list
panstwa = ["Polska", "Niemcy", "Francja", "Hiszpania"]
stolice = ["Warszawa", "Berlin", "Paryz", "Madryt"]

slownik = {panstwo:stolica for panstwo, stolica in zip(panstwa, stolice) }
print(slownik)

teksty = [f'{panstwo} ma stolicę w mieście {stolica}' for panstwo, stolica in zip(panstwa, stolice)]
print(teksty)