class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def drive(self, km):
        self.mileage += km

    def info(self):
        print(f"Марка: {self.brand}")
        print(f"Рік випуску: {self.year}")
        print(f"Пробіг: {self.mileage} км")

    def __str__(self):
        return f"{self.brand} ({self.year}), пробіг: {self.mileage} км"


# Створення об’єктів класу Car
car1 = Car("Toyota", 2018, 45000)
car2 = Car("BMW", 2020, 30000)

# Збільшення пробігу
car1.drive(150)
car2.drive(500)

# Виведення інформації
car1.info()
print(car1)

print()
car2.info()
print(car2)
