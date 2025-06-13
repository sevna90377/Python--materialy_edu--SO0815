zbior = {5,2,7,8,1}

#dodawanie el.
zbior.add(9)
print("Zbiór po dodaniu elementu:")
print(zbior)

#usuwanie el.
zbior.remove(2)
print("Zbiór po usunięciu elementu:")
print(zbior)

#usuwanie el. JEŚLI ISTNIEJE
zbior.discard(44)
print("Zbiór po probie usuniecia nieistniejącego el:")
print(zbior)

#zwrócenie el. (zostanie usunięty)
jakis_element = zbior.pop()
print(f"Zwrócony element: {jakis_element}, zbiór po operacji: {zbior}")

#usunięcie wszystkich
zbior.clear()