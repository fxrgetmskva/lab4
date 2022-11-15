import random
punkty = []
for b in range(15):
    a =  random.uniform (0 , 50)
    c = round(a, 2)
    punkty.append(c)
print(punkty)
print(" maksymałna liczba punktów",max(punkty))
print("minimałna liczba punktów:",min(punkty))