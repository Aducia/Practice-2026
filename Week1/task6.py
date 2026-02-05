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


# Створення об’єктів
animals = [Dog(), Cat(), Rooster()]

# Виклик перевизначеного методу
for animal in animals:
    print(animal.sound())