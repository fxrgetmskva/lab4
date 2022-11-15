import random
punkty = [round(random.uniform(0,50), 2) for i in range(15)]
print(punkty)
print(max(punkty) , min(punkty))
g = float(input("Prosze podać liczbe punktów;"))
if g in punkty:
    print(punkty.index(g))
else:
    print("Brak  wartości w lisćie")
b = sum(punkty)/len(punkty)
b = round(b,2)
print("srednie: ", b )

list1 = []
for i in punkty:
    if i  < b:
        list1.append(1)
print(len(list1))
print(list1)

list2 = [i for i in punkty if i > b]
print(lem(list2))
print(list2)