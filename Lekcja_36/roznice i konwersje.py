
lista   = [1,2,3]
krotka  = (4,5,6)
zbior   = {7,8,9}
slownik = {
    1 : "a",
    2 : "b",
    3 : "c",
    4 : "d"
}


# Konwersje

print("zbiór -> lista")
print(list(zbior))
print(type(list(zbior)))

print("krotka -> lista")
print(list(krotka))
print(type(list(krotka)))

print("zbiór -> krotka")
print(tuple(zbior))
print(type(tuple(zbior)))

print("lista -> krotka")
print(tuple(lista))
print(type(tuple(lista)))

print("krotka -> zbior")
print(set(krotka))
print(type(set(krotka)))

print("lista -> zbior")
print(set(lista))
print(type(set(lista)))