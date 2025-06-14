''' Zadanie 1. 

Napisz funkcję <dzielenie_i_mnożenie> przyjmującą dwie wartości a i b, która
wyświetli wynik działania a / b oraz a * b. Co się wydarzy jeżeli nie zaimplementujemy
obsługi wyjątków i spróbujemy dzielić przez 0?
'''

def dzielenie_i_mnozenie(a, b):
    try:
        a/b
    except Exception as e:
        print(e)
    else:
        print(f"Wynik dzielenia {a} / {b} = {a/b}")
    finally:
        print(f"Wynik mnozenia {a} * {b} = {a*b}")

dzielenie_i_mnozenie(5, 0)

