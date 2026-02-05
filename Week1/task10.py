from abc import ABC, abstractmethod

# Абстрактний базовий клас
class LibraryItem(ABC):
    def __init__(self, title):
        self._title = title

    @abstractmethod
    def info(self):
        pass


# Клас Книга
class Book(LibraryItem):
    def __init__(self, title, pages):
        super().__init__(title)
        self.pages = pages   # звернення через property

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if value < 0:
            raise ValueError("Кількість сторінок не може бути від’ємною")
        self._pages = value

    def info(self):
        return f"Книга: {self._title}, сторінок: {self.pages}"


# Демонстрація роботи
book1 = Book("Як приборкати дракона", 232)
print(book1.info())
book2 = Book("«Як приборкати дракона. Книжка 2. Як стати піратом»", 224)
print(book2.info())
# Спроба встановити некоректне значення
# book1.pages = -50   # викличе помилку
