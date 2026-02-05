from abc import ABC, abstractmethod

# Абстрактний базовий клас (абстракція)
class LibraryItem(ABC):
    def __init__(self, title):
        self.__title = title        # інкапсуляція (приватний атрибут)

    def get_title(self):
        return self.__title

    @abstractmethod
    def info(self):
        pass


# Похідний клас (наслідування)
class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    # Поліморфізм: власна реалізація методу
    def info(self):
        return f"Книга: {self.get_title()}, автор: {self.author}"


# Клас читача
class Reader:
    def __init__(self, name):
        self.name = name
        self.books = []   # список взятих книг

    def take_book(self, book):
        self.books.append(book)
        print(f"{self.name} взяв(ла) книгу «{book.get_title()}»")

    def show_books(self):
        print(f"\nКниги читача {self.name}:")
        for book in self.books:
            print(book.info())   # поліморфний виклик


# Демонстрація взаємодії об’єктів
book1 = Book("Місто", "Валер’ян Підмогильний")
book2 = Book("1984", "Джордж Орвелл")

reader = Reader("Влада")

reader.take_book(book1)
reader.take_book(book2)
reader.show_books()
