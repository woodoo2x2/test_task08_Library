import json
import os


class Book:
    """Класс для представления книги."""

    def __init__(self, id,  title, author, year):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = True


    def to_dict(self):
        """Преобразует объект книги в словарь."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }


class Library:

    def __init__(self):
        self.books = []
        if not os.path.exists('library.json'):
            with open('library.json', 'w', encoding='utf-8') as library_json:
                json.dump({}, library_json, indent=4, ensure_ascii=False)
        else:
            with open('library.json', "r", encoding="utf-8") as file:
                data = json.load(file)
                self.books = [i for i in data]

    def add_book(self,title,author,year):
        if self.books:
            id = self.books[-1]['id'] + 1
        else:
            id = 1


        self.books.append(Book(id,title, author, year).to_dict())

        with open('library.json', 'w', encoding='utf-8') as library_json:
            json.dump(self.books, library_json, indent=4, ensure_ascii=False)

    def delete_book_by_id(self,id):

        with open('library.json', 'r', encoding='utf-8') as library_json:
            self.books = json.load(library_json)

        updating_books = [book for book in self.books if book['id'] != id]
        if updating_books == self.books:
            raise ValueError('Такой книги нет в библиотеке')
        else:
            with open('library.json', 'w',encoding='utf-8') as library_json:
                json.dump(updating_books, library_json, indent=4, ensure_ascii=False)

    def show_all_books(self):
        return self.books

    def find_book_by_id(self,id):
        #id = int(input())
        for book in self.books:
            if book['id'] == id:
                return book
        return "Книги по такому номеру нет в базе"

    def find_book_by_title(self,title):
        #title = input()
        for book in self.books:
            if book['title'] == title:
                return book
        return "Книги по такому номеру названию нет в базе"

    def find_book_by_author(self,author):
        #author = input()
        for book in self.books:
            if book['author'] == author:
                return book
        return "Книги по такому номеру названию нет в базе"

lb = Library()
lb.show_all_books()

