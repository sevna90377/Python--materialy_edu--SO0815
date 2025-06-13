# Listy
### cechy:
 - dynamiczne rozmiary - lista może zmieniać swoją długość w trakcie działania programu; jest zawsze dopasowana do zawartości
 - indeksowanie - elementy listy są uporządkowane i można się do nich dostać przy użyciu indeksów, np. lista[0]
 - zmienność - można zmieniać ich zawartość po utworzeniu
 - mieszane typy danych - mogą przechowywać różne typy jednocześnie (liczby całkowite, łańcuchy, etc, a nawet inne listy)

## Rozgrzewka
Napisz program w którym stworzysz listę z 10 liczbami, a następnie wypiszesz co
drugą z nich.

## Metody list
### tworzenie listy
```Python
lista = ["aaa", 78, 3.5, 'fortnite']
```
### dodawanie elementów
zostają doklejone na końcu listy
```Python
lista.append(-6)
```
### dodanie elementów iterable z "rozpakowaniem"
czyli np. lista zostanie dodana element po elemencie na końcu
```Python
lista.extend(["pies","Marek",25])
```
### umieszczenie elementu pod indeksem
```Python
lista.insert(1, "fortnite")
```
### usunięcie danego elementu
jeśli danego elementu nie ma, pojawi się wyjątek ValueError
```Python
lista.remove("aaa")
```
### usunięcie elementu spod indeksu
jeśli nie ma elementu pod danym indeksem, pojawi się wyjątek IndexError
element jest zwracany (można np. przypisać go do zmiennej)
```Python
a = lista.pop(1)
```
### znajdowanie indeksu elementu
jeśli danego elementu nie ma, pojawi się wyjątek ValueError
można określić dodatkowo zakres poszukiwań
```Python
lista.index("fortnite")
lista.index("fortnite", 3)
lista.index("fortnite", 3, 6)
```
### zliczanie wystąpień
```Python
liczba = lista.count("fortnite")
``` 

### sortowanie
Nie można posortować list o mieszanych typach, bo jak porównać liczbę i słowo?
```Python
lista.sort()
```
### odwrócenie kolejności
```Python
lista.reverse()
```
### kopiowanie listy
Będzie to kopia płytka listy
```Python
listaB = lista.copy()
```
### czyszczenie listy
```Python
lista.clear()
``` 