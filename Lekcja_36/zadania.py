lista   = [1,2,3]
krotka  = (4,5,6)
zbior   = {7,8,9}
slownik = {
    1 : "a",
    2 : "b",
    3 : "c"
}

print(f"Dlugość listy: {len(lista)}")
print(f"Dlugość krotki: {len(krotka)}")

for item in slownik:
    print(item)

for item in slownik.values():
    print(item)

print(lista[::-1])

for item in lista[::-1]:
    print(item)