import json
import os


class Book:
    """Класс для представления книги."""

    def __init__(self, id: int, title: str, author: str, year: int) -> None:
        self.id: int = id
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: bool = True

    def to_dict(self) -> dict:
        """Преобразует объект книги в словарь."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }


class Library:
    def __init__(self, filename: str = 'library.json') -> None:
        self.filename: str = filename
        self.books: list = self._load_books()

    def _load_books(self) -> list:
        """Загружает книги из файла."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []

    def _save_books(self) -> None:
        """Сохраняет книги в файл."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.books, file, indent=4, ensure_ascii=False)

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавляет новую книгу в библиотеку."""
        new_id = self.books[-1]['id'] + 1 if self.books else 1
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book.to_dict())
        self._save_books()

    def delete_book_by_id(self, book_id: int) -> None:
        """Удаляет книгу по ID."""
        self.books = [book for book in self.books if book['id'] != book_id]
        self._save_books()

    def show_all_books(self) -> list:
        """Показывает все книги в библиотеке."""
        return self.books

    def find_book_by_year(self, year: int) -> list:
        """Поиск книги по году."""
        return [book for book in self.books if book['year'] == year]

    def change_book_status_by_id(self, book_id: int) -> None:
        """Меняет статус книги по ID."""
        book = next((book for book in self.books if book['id'] == book_id), None)
        if book:
            book['status'] = not book['status']
            self._save_books()

    def find_book_by_id(self, book_id: int) -> int:
        """Ищет книгу по ID."""
        for book in self.books:
            if book['id'] == book_id:
                return book

    def find_book_by_title(self, title: str) -> dict:
        """Ищет книгу по названию."""
        for book in self.books:
            if book['title'] == title:
                return book

    def find_book_by_author(self, author: str) -> list:
        """Ищет книги по автору."""
        return [book for book in self.books if book['author'] == author]
