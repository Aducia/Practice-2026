import math

v = float(input("Введіть початкову швидкість v (м/с): "))
angle_deg = float(input("Введіть кут вильоту (градуси): "))

g = 9.81
angle_rad = math.radians(angle_deg)

R = (v ** 2) * math.sin(2 * angle_rad) / g
R_rounded = round(R)

print("Дальність польоту:", R_rounded, "м")
print("Максимальна дальність (за цього v) досягається при куті 45°.")
