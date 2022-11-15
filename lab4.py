zwierzeta = []
y = 0
while y < 4:
    x = input(" Podaj nazwe zwierzeta: ")
    zwierzeta.append(x)
    y += 1
print(zwierzeta)
a = sorted(zwierzeta)
print(a)
print(zwierzeta[0], zwierzeta[-3:1])
print(zwierzeta.sort())
print(len(zwierzeta))
