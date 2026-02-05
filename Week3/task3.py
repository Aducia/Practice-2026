import math

a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

d = b**2 - 4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Два корені:")
    print("x1 =", x1)
    print("x2 =", x2)
elif d == 0:
    x = -b / (2*a)
    print("Один корінь:")
    print("x =", x)
else:
    print("Дійсних коренів немає")
