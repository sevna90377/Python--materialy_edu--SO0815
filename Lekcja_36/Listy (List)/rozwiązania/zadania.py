x = [1, 2, 3]
y = [4, 5, 6]

x.extend(y)

x.pop(5)
x.pop(2)

x.remove(min(x))
x.remove(max(x))

x.append(6)

x.sort()

y = x.copy()

y.reverse()

for i in range(len(x)):
    x[i] += 1

for i in range(len(y)):
    y[i] -= 1

print(x, y)