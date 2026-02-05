class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Гав-гав"


class Cat(Animal):
    def sound(self):
        return "Мяу"


class Rooster(Animal):
    def sound(self):
        return "Кукарєкуу"


animals = [Dog(), Cat(), Rooster()]

print("Звуки тварин:\n")

for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.sound()}")
